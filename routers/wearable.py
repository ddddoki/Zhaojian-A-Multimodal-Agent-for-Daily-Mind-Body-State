from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Wearable

router = APIRouter(prefix="/wearable", tags=["穿戴设备"])

class WearableForm(BaseModel):
    username: str
    device_sn: str
    device_type: str
    is_online: bool

@router.post("/bind")
def bind_device(w: WearableForm, db: Session = Depends(get_db)):
    new_dev = Wearable(
        username=w.username,
        device_sn=w.device_sn,
        device_type=w.device_type,
        is_online=w.is_online
    )
    db.add(new_dev)
    db.commit()
    db.refresh(new_dev)
    return {"msg": "设备绑定成功", "data": new_dev}

@router.get("/list/{username}")
def get_device_list(username: str, db: Session = Depends(get_db)):
    devs = db.query(Wearable).filter(Wearable.username == username).all()
    if not devs:
        raise HTTPException(status_code=400, detail="该用户暂无绑定设备")
    return {"msg": "查询成功", "data": devs}