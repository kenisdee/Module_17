from sqlalchemy import Column, Integer, String, event
from sqlalchemy.orm import relationship
from backend.db import Base

class User(Base):
    __tablename__ = 'users'

    username = Column(String, unique=True, index=True)
    firstname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    lastname = Column(String)
    id = Column(Integer, primary_key=True, index=True)

    tasks = relationship("Task", back_populates="user")

@event.listens_for(User, 'before_insert')
@event.listens_for(User, 'before_update')
def set_slug(mapper, connection, target):
    target.slug = target.username