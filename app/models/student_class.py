from sqlalchemy import Column, Integer, ForeignKey
from app.database.database import Base

class StudentClass(Base):
    __tablename__ = "student_class"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("dance_classes.id"))