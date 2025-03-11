from db.schemas import Employee
from services.employee_service import employees_db, create_emp_details, update_emp_details, del_emp_details, get_emp_details
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/employees", tags=['employees'])

@router.get("/")
async def get_employees():
    return employees_db

@router.get("/{employee_id}")
async def get_employee(employee_id: int):
    employee = get_emp_details(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.post("/")
async def create_employee(employee: Employee):
    new_employee = create_emp_details(employee)
    return new_employee

@router.put("/update/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    updated_employee = update_emp_details(employee_id, employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.delete("/delete/{employee_id}")
async def delete_employee(employee_id: int):
    deleted_employee = del_emp_details(employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_employee