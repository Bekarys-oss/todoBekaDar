# from pydantic import BaseModel

# class User(BaseModel):
#     username: str
#     password: str

#     class Config:
#         from_attributes = True

# class UserCreate(BaseModel):
#     username: str
#     password: str

# class UserResponse(BaseModel):
#     id: int
#     username: str

#     class Config:
#         from_attributes = True

# class TaskBase (BaseModel):
#     title: str
#     description: str | None = None

# class TaskCreate(TaskBase):
#     pass

# class TaskResponse (TaskBase):
#     id: int
#     completed: bool
#     owner_id: int

#     class Config:
#         from_attributes = True


from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
    
class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool
    owner_id: int

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# class StudenCreate():
#     FirstName: str
#     LastName: str
#     Group: int
#     City: str

# class StudentResponse():
#     id: int
#     LastName: str