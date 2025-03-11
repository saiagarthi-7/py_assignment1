from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import get_db
from services.department_service import get_dept_details, create_dept_details, update_dept_details, del_dept_details
from db.schemas import Department

router = APIRouter(prefix="/departments", tags=["departments"])

@router.get("/{department_id}")
async def get_department(department_id: int, db: Session = Depends(get_db)):
    return get_dept_details(department_id, db)

@router.post("/create")
async def create_department(department: Department, db: Session = Depends(get_db)):
    return create_dept_details(department, db)

@router.put("/update/{department_id}")
async def update_department(department_id: int, department: Department, db: Session = Depends(get_db)):
    return update_dept_details(department_id, department, db)

@router.delete("/delete/{department_id}")
async def delete_department(department_id: int, db: Session = Depends(get_db)):
    return del_dept_details(department_id, db)