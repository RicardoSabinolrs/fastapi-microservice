from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED

from app.api.api_v1.deps.repository import get_repository
from app.crosscutting.exceptions.database import EntityAlreadyExists
from app.crosscutting.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)
from app.domain.repository.crud.account import AccountCRUDRepository
from app.domain.schemas.account import AccountInCreate, AccountInLogin, AccountInResponse, AccountWithToken
from app.infra.security.authorizations.jwt import jwt_generator

router = APIRouter()


@router.post(
    "/signup",
    name="auth:signup",
    response_model=AccountInResponse,
    status_code=HTTP_201_CREATED,
)
async def signup(
        account_create: AccountInCreate,
        account_repo: AccountCRUDRepository = Depends(get_repository(repo_type=AccountCRUDRepository)),
) -> AccountInResponse:
    try:
        await account_repo.is_username_taken(username=account_create.username)
        await account_repo.is_email_taken(email=account_create.email)

    except EntityAlreadyExists:
        raise await http_exc_400_credentials_bad_signup_request()

    new_account = await account_repo.create_account(account_create=account_create)
    access_token = jwt_generator.generate_access_token(account=new_account)

    return AccountInResponse(
        id=new_account.id,
        authorized_account=AccountWithToken(
            token=access_token,
            username=new_account.username,
            email=new_account.email,
            is_verified=new_account.is_verified,
            is_active=new_account.is_active,
            is_logged_in=new_account.is_logged_in,
            created_at=new_account.created_at,
            updated_at=new_account.updated_at,
        ),
    )


@router.post(
    path="/signin",
    name="auth:signin",
    response_model=AccountInResponse,
    status_code=HTTP_202_ACCEPTED,
)
async def signin(
        account_login: AccountInLogin,
        account_repo: AccountCRUDRepository = Depends(get_repository(repo_type=AccountCRUDRepository)),
) -> AccountInResponse:
    try:
        db_account = await account_repo.read_user_by_password_authentication(account_login=account_login)

    except Exception:
        raise await http_exc_400_credentials_bad_signin_request()

    access_token = jwt_generator.generate_access_token(account=db_account)

    return AccountInResponse(
        id=db_account.id,
        authorized_account=AccountWithToken(
            token=access_token,
            username=db_account.username,
            email=db_account.email,
            is_verified=db_account.is_verified,
            is_active=db_account.is_active,
            is_logged_in=db_account.is_logged_in,
            created_at=db_account.created_at,
            updated_at=db_account.updated_at,
        ),
    )
