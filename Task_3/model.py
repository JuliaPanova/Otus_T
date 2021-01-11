from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Post(base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer)
    title = Column(String)
    body = Column(String)
