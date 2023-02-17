import datetime

import pydantic

from app.domain.schemas.base import BaseSchemaModel


class AccountInCreate(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "sabino",
                "email": "sabino@teste.com",
                "password": "123456"
            }
        }


class AccountInUpdate(BaseSchemaModel):
    username: str | None
    email: str | None
    password: str | None

    class Config:
        schema_extra = {
            "example": {
                "username": "sabino",
                "email": "teste@teste.com",
                "password": "123456"
            }
        }


class AccountInLogin(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "sabino",
                "email": "teste@teste.com",
                "password": "123456"
            }
        }


class AccountWithToken(BaseSchemaModel):
    token: str
    username: str
    email: pydantic.EmailStr
    is_verified: bool
    is_active: bool
    is_logged_in: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

    class Config:
        schema_extra = {
            "example": {
                "token": "sabino",
                "username": "teste@teste.com",
                "email": "123456",
                "is_verified": True,
                "is_active": True,
                "is_logged_in": True,
                "created_at": "2023-02-14",
                "updated_at": None,
            }
        }


class AccountInResponse(BaseSchemaModel):
    id: int
    authorized_account: AccountWithToken

    class Config:
        schema_extra = {
            "example": {
                "id": "123456",
                "authorized_account": "hdWle52zSRvdVjCfG9shtBsMbhFcvETReIewkjeWplSU81rrVePDe72SNNhB08AQV0QLETC"
            }
        }

