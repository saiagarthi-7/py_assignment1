from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_all_departments(db: Session):
    return db.query(models.Department).order_by(models.Department.id).all()

def get_dept_details(dept_id: int, db: Session):
    department = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if department:
        return department
    else:
        raise HTTPException(status_code=404, detail='Department ID not found')

def create_dept_details(dept: schemas.Department, db: Session):
    try:
        existing_dept = db.query(models.Department).filter(models.Department.id == dept.id).first()
        if existing_dept:
            raise HTTPException(status_code=400, detail='Department ID already existed')

        existing_dept_name = db.query(models.Department).filter(models.Department.name == dept.name).first()
        if existing_dept_name:
            raise HTTPException(status_code=404, detail='department name already existed')
        db_dept = models.Department(**dept.model_dump())
        db.add(db_dept)
        db.commit()
        db.refresh(db_dept)
        return {'message':'department added successfully'}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def update_dept_details(dept_id: int, dept: schemas.DepartmentUpdate, db: Session):
    department = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if department:
        department.name = dept.name
        db.commit()
        db.refresh(department)
        return {'message':'department name updated successfully'}
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