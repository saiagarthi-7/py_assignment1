from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_salary_details(emp_id: int, db: Session):
    salary = db.query(models.Salary).filter(models.Salary.emp_id == emp_id).first()
    if salary:
        return salary
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')

def create_salary_details(salary: schemas.Salary, db: Session):
    db_salary = models.Salary(**salary.model_dump())
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)
    return db_salary

def update_salary_details(emp_id: int, salary: schemas.SalaryUpdate, db: Session):
    salary_record = db.query(models.Salary).filter(models.Salary.emp_id == emp_id).first()
    if salary_record:
        salary_record.amount = salary.amount
        db.commit()
        db.refresh(salary_record)
        return salary_record
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')

def del_salary_details(emp_id: int, db: Session):
    salary_record = db.query(models.Salary).filter(models.Salary.emp_id == emp_id).first()
    if salary_record:
        db.delete(salary_record)
        db.commit()
        return {'successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail='Salary details not found')