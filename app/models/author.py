from pydantic import BaseModel
from sqlalchemy import Column, String
from .ormbase import OrmBase

class Author(OrmBase, BaseModel):
    name: Column(String)
    genre: Column(String)