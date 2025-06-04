from sqlalchemy import Column, Integer, String,ForeignKey
from app.database.database import Base
from sqlalchemy.orm import relationship 

class DanceClass(Base):
    __tablename__ = "dance_classes"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, unique=True, nullable=False)
    dance_style = Column(String, nullable=False)
    schedule = Column(String, nullable=False) # e.g., Mon-Wed-Fri 6PM
    instructor_id = Column(Integer, ForeignKey("instructors.id"))  
    instructor = relationship("Instructor", backref="classes")