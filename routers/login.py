from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()

class LoginForm(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(form: LoginForm, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or user.hashed_password != form.password:
        raise HTTPException(status_code=400, detail="用户名或密码错误")
    return {"msg":"登录成功", "username": user.username}
