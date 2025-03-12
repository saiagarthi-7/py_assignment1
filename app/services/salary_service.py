from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_salary_details(emp_id: int, db: Session):
    amnt = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if amnt.salary:
        return amnt.salary
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')

# def create_salary_details(salary: schemas.Employee, db: Session):
#     db_salary = models.Employee(**salary.model_dump())
#     db.add(db_salary)
#     db.commit()
#     db.refresh(db_salary)
#     return db_salary

def update_salary_details(emp_id: int, salary: schemas.SalaryUpdate, db: Session):
    salary_record = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if salary_record.salary:
        salary_record.salary = salary.amount
        db.commit()
        return {'message':'Salary updated'}
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')

def del_salary_details(emp_id: int, db: Session):
    salary_record = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if salary_record:
        db.delete(salary_record)
        db.commit()
        return {'successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')