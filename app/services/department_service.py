from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_dept_details(dept_id: int, db: Session):
    department = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if department:
        return department
    else:
        raise HTTPException(status_code=404, detail='Department ID not found')

def create_dept_details(dept: schemas.Department, db: Session):
    db_dept = models.Department(**dept.model_dump())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def update_dept_details(dept_id: int, dept: schemas.Department, db: Session):
    department = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if department:
        department.name = dept.name
        db.commit()
        db.refresh(department)
        return department
    else:
        raise HTTPException(status_code=404, detail='Department ID not found')

def del_dept_details(dept_id: int, db: Session):
    department = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if department:
        db.delete(department)
        db.commit()
        return {'successfully  deleted'}
    else:
        raise HTTPException(status_code=404, detail='Department ID not found')