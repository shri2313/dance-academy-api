from sqlalchemy import Column, Integer, String, Date
from app.database.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    dance_style = Column(String)
    # age = Column(Integer)
