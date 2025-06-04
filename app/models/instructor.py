from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    expertise = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)