from sqlalchemy import Column, String, Integer

from app.db.base_class import Base


class Beer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), index=True)
    ibu = Column(Integer, index=True)
    style = Column(String(256), index=True)
    description = Column(String(256))
    alcohol_tenor = Column(String(256), index=True)
