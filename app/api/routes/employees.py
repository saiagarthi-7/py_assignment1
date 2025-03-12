from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.employee_service import get_all_employees, get_emp_details, create_emp_details, update_emp_details, del_emp_details
from db.schemas import EmployeeCreate, EmployeeUpdate, Employee

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/")
async def get_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)

@router.get("/{employee_id}")
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        return get_emp_details(employee_id, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=404, detail="Employee Not Found")

@router.post("/create")
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return create_emp_details(employee, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/update/{employee_id}")
async def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    try:
        return update_emp_details(employee_id, employee, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        return del_emp_details(employee_id, db)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")