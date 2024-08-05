from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from models.user import User
from schemas import CreateUser, UpdateUser


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
def all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{user_id}")
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "username": user.username,
        "firstname": user.firstname,
        "age": user.age,
        "slug": user.username,
        "lastname": user.lastname,
        "id": user.id,
    }

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/{user_id}")
def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None
    db.commit()
    db.refresh(db_user)
    return {
        "username": db_user.username,
        "firstname": db_user.firstname,
        "age": db_user.age,
        "slug": db_user.username,  # Assuming slug is the same as username
        "lastname": db_user.lastname,
        "id": db_user.id,
    }

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}