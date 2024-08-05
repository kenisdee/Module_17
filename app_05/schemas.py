from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int

class TaskCreate(BaseModel):
    title: str
    content: str
    priority: int

class TaskUpdate(BaseModel):
    title: str
    content: str
    priority: int