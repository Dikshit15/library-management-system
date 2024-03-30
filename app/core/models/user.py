from pydantic import BaseModel
from sqlalchemy import Column, String
from .ormbase import OrmBase

class User(OrmBase, BaseModel):
    name: Column(String)
    email: Column(String)
    phone: Column(String)