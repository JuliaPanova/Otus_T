from sqlalchemy import Column, Integer, String, Boolean

from .database import db

class Contact(db.Model):
    __tablename__ = 'contacts'
    __table_args__ = {'schema': 'myclass'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    team_id = Column(Integer)
    name = Column(String)
    phone = Column(String)
