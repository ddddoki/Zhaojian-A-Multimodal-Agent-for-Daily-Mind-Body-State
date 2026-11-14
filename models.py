from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, comment="用户名")
    hashed_password = Column(String, comment="加密后的密码")

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    heart_rate = Column(Integer)
    blood_pressure_high = Column(Integer)
    blood_pressure_low = Column(Integer)
    step = Column(Integer)

class Wearable(Base):
    __tablename__ = "wearables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    device_sn = Column(String)
    device_type = Column(String)
    is_online = Column(Integer)