import datetime

import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions

from app.infra.database.metadata_orm import Base


class Beer(Base):
    __tablename__ = "beer"

    id: SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True, autoincrement="auto")
    name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(
        sqlalchemy.String(length=200), nullable=False, unique=False
    )
    ibu: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=5), nullable=False)
    style: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=200), nullable=False)
    description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=200), nullable=False)
    alcohol_tenor: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=5), nullable=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )
