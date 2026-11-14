from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()

class RegisterForm(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(form: RegisterForm, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.username == form.username).first()
    if exist_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    new_user = User(
        username=form.username,
        hashed_password=form.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "注册成功", "username": new_user.username}
