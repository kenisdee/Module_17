from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router
from backend.db import engine, Base
from models import User, Task
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

# Function to initialize database
def initialize_database():
    Base.metadata.create_all(bind=engine)
    from sqlalchemy.schema import CreateTable
    logger.info(CreateTable(User.__table__).compile(engine))
    logger.info(CreateTable(Task.__table__).compile(engine))

# Initialize database
initialize_database()