from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_emp_details(emp_id: int, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail='Employee ID not found')

def create_emp_details(emp: schemas.EmployeeCreate, db: Session):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def update_emp_details(emp_id: int, emp: schemas.Employeeupdate, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if employee:
        employee.name = emp.name
        employee.email = emp.email
        employee.position = emp.position
        employee.salary = emp.salary
        db.commit()
        db.refresh(employee)
        return employee
    else:
        raise HTTPException(status_code=404, detail='Employee ID not found')

def del_emp_details(emp_id: int, db: Session):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return {'successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail='Employee ID not found')