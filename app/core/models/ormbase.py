from pydantic import BaseModel
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, BigInteger, String, DateTime

class OrmBase(BaseModel):
    id =  Column(BigInteger, primary_key=True)
    createdAt: Column(DateTime)
    updatedAt: Column(DateTime)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    