from pydantic import BaseModel
from sqlalchemy import Column, BigInteger
from .ormbase import OrmBase

class Book(OrmBase, BaseModel):
    name: Column(BigInteger)
    genre: Column(BigInteger)
    authorId: Column(BigInteger)