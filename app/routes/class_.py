from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.class_ import DanceClassCreate, DanceClassResponse
from app.models.class_ import DanceClass
from app.database.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/classes", tags=["Dance Classes"])

@router.post("/", response_model=DanceClassResponse)
def create_class(class_data: DanceClassCreate, db: Session = Depends(get_db)):
    dance_class = DanceClass(**class_data.dict())
    db.add(dance_class)
    db.commit()
    db.refresh(dance_class)
    return dance_class

@router.get("/", response_model=list[DanceClassResponse])
def get_all_classes(db: Session = Depends(get_db)):
    return db.query(DanceClass).all()

@router.put("/{class_id}/instructor/{instructor_id}")
def assign_instructor(class_id: int, instructor_id: int, db: Session = Depends(get_db)):
    dance_class = db.query(DanceClass).filter(DanceClass.id == class_id).first()
    if not dance_class:
        raise HTTPException(status_code=404, detail="Class not found")

    dance_class.instructor_id = instructor_id
    db.commit()
    return {"message": f"Instructor {instructor_id} assigned to class {class_id}"}