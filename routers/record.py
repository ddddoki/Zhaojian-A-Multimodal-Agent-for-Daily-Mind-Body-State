from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Record

router = APIRouter(prefix="/record", tags=["健康记录"])

# 提交记录需要传的数据
class RecordForm(BaseModel):
    username: str
    heart_rate: int       # 心率
    blood_pressure_high: int  # 收缩压（高压）
    blood_pressure_low: int   # 舒张压（低压）
    step: int             # 步数

# 新增一条健康记录
@router.post("/add")
def add_record(record: RecordForm, db: Session = Depends(get_db)):
    new_record = Record(
        username=record.username,
        heart_rate=record.heart_rate,
        blood_pressure_high=record.blood_pressure_high,
        blood_pressure_low=record.blood_pressure_low,
        step=record.step
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"msg": "记录添加成功", "data": new_record}

# 根据用户名查询所有记录
@router.get("/list/{username}")
def get_record_list(username: str, db: Session = Depends(get_db)):
    records = db.query(Record).filter(Record.username == username).all()
    if not records:
        raise HTTPException(status_code=400, detail="暂无该用户记录")
    return {"msg": "查询成功", "data": records}
