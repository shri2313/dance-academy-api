from pydantic import BaseModel

class StudentClassLink(BaseModel):
    student_id: int
    class_id: int

