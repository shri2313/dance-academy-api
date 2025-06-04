from pydantic import BaseModel, EmailStr

class InstructorBase(BaseModel):
    full_name: str
    expertise: str
    contact: str
    email: EmailStr

class InstructorCreate(InstructorBase):
    pass

class InstructorResponse(InstructorBase):
    id: int

    class Config:
        orm_mode = True