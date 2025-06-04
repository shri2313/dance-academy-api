from pydantic import BaseModel
from datetime import date

# Shared fields between create and response
class StudentBase(BaseModel):
    full_name: str
    email: str
    phone_number: str
    dance_style: str
    # age: int

# For creating new students
class StudentCreate(StudentBase):
    pass

# For responses (includes ID)
class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True