from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.instructor import Instructor
from app.schemas.instructor import InstructorCreate, InstructorResponse
from app.database.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/instructors", tags=["Instructors"], dependencies=[Depends(get_current_user)])

@router.post("/", response_model=InstructorResponse)
def create_instructor(data: InstructorCreate, db: Session = Depends(get_db)):
    instructor = Instructor(**data.dict())
    db.add(instructor)
    db.commit()
    db.refresh(instructor)
    return instructor

@router.get("/{instructor_id}", response_model=InstructorResponse)
def get_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

@router.put("/{instructor_id}", response_model=InstructorResponse)
def update_instructor(instructor_id: int, updated: InstructorCreate, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    for key, value in updated.dict().items():
        setattr(instructor, key, value)
    db.commit()
    db.refresh(instructor)
    return instructor

@router.delete("/{instructor_id}")
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    instructor = db.query(Instructor).filter(Instructor.id == instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db.delete(instructor)
    db.commit()
    return {"message": "Instructor deleted successfully"}
