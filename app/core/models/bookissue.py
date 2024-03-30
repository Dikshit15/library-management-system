from pydantic import BaseModel
from sqlalchemy import Column, BigInteger, DateTime, Integer
from .ormbase import OrmBase

class BookIssue(OrmBase, BaseModel):
    bookId: Column(BigInteger)
    userId: Column(BigInteger)
    issueDate: Column(DateTime)
    dueDate: Column(DateTime)
    returnDate: Column(DateTime)
    fineCollected: Column(Integer)