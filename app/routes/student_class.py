from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.student_class import StudentClass
from app.models.student import Student
from app.models.class_ import DanceClass
from app.database.database import get_db
from app.schemas.student_class import StudentClassLink
from app.schemas.student import StudentResponse
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/enrollments",
    tags=["Student-Class Enrollment"]
)

@router.post("/")
def enroll_student(link: StudentClassLink, db: Session = Depends(get_db)):
    # Check if student and class exist
    student = db.query(Student).filter(Student.id == link.student_id).first()
    dance_class = db.query(DanceClass).filter(DanceClass.id == link.class_id).first()

    if not student or not dance_class:
        raise HTTPException(status_code=404, detail="Student or Class not found")

    enrollment = StudentClass(student_id=link.student_id, class_id=link.class_id)
    db.add(enrollment)
    db.commit()
    return {"message": "Student enrolled in class successfully"}

@router.get("/class/{class_id}/students", response_model=list[StudentResponse])
def get_students_in_class(class_id: int, db: Session = Depends(get_db)):
    # Step 1: Get all student_ids from the join table
    student_links = db.query(StudentClass).filter(StudentClass.class_id == class_id).all()
    student_ids = [link.student_id for link in student_links]

    # Step 2: Query students using those IDs
    students = db.query(Student).filter(Student.id.in_(student_ids)).all()
    return students