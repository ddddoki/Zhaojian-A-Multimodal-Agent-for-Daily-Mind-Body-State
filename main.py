from fastapi import FastAPI
from routers import login, user,record,wearable

app = FastAPI(title="用户后端")

app.include_router(login.router)
app.include_router(user.router)
app.include_router(record.router)
app.include_router(wearable.router)

# 导入models，自动建表
from database import engine
from models import Base
Base.metadata.create_all(bind=engine)
