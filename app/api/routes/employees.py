from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import get_db
from services.employee_service import get_emp_details, create_emp_details, update_emp_details, del_emp_details
from db.schemas import Employee

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/{employee_id}")
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_emp_details(employee_id, db)

@router.post("/create")
async def create_employee(employee: Employee, db: Session = Depends(get_db)):
    return create_emp_details(employee, db)

@router.put("/update/{employee_id}")
async def update_employee(employee_id: int, employee: Employee, db: Session = Depends(get_db)):
    return update_emp_details(employee_id, employee, db)

@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return del_emp_details(employee_id, db)