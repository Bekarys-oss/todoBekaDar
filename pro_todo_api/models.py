from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# class Student(Base):
#     id= Column (Integer, primary_key=True, index=True)
#     firstName= Column (String, index=True, nullable=False)
#     lastName= Column (String, index=True, nullable=False)
#     group = Column (Integer, index=True)
#     City = Column (String, index=True,)


class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)
    username = Column (String, unique=True, index=True, nullable=False)
    hashed_password = Column (String, nullable=False)
    tasks = relationship ("Task", back_populates="owner")

class Task(Base):
    __tablename__="tasks"

    id = Column (Integer, primary_key=True, index=True)
    title = Column (String, index=True, nullable=False)
    description = Column (String, nullable= True)
    completed = Column (Boolean, default=False)
    owner_id = Column (Integer, ForeignKey("users.id"))
    owner = relationship ("User", back_populates ="tasks")