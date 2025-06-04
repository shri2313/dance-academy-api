from pydantic import BaseModel
from typing import Optional
from app.schemas.instructor import InstructorResponse

class DanceClassBase(BaseModel):
    class_name: str
    dance_style: str
    schedule: str

class DanceClassCreate(DanceClassBase):
    instructor_id: Optional[int] = None 

class DanceClassResponse(DanceClassBase):
    id: int
    instructor_id: Optional[int]
    instructor: Optional[InstructorResponse] 

    class Config:
        orm_mode = True