from db.schemas import Employee
from services.employee_service import employees_db, create_emp_details,update_emp_details,del_emp_details,get_emp_details
from fastapi import APIRouter

router = APIRouter(prefix="/product", tags=['product'])


@router.get('/')
def get_all():
    return employees_db

@router.get("/employee/{employee_id}")
def get_employee(emp_id:int):
        return get_emp_details(emp_id)
       

@router.post('/employee')
def emp_details(emp:Employee):
    return create_emp_details(emp)


@router.put('/employee')
def updated_emp(emp_id:int,name:str):
    return update_emp_details(emp_id,name)


@router.delete('/employee/{emp_id}')
def delete_emp(emp_id:int):
    return del_emp_details(emp_id)