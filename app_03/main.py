from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router
from backend.db import engine, Base
from models import User, Task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Импорт необходимых функций для вывода SQL запросов
from sqlalchemy.schema import CreateTable

# Вывод SQL запросов для создания таблиц
print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))