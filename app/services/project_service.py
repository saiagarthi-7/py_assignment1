from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas, database

def get_all_projects(db: Session):
    return db.query(models.Project).order_by(models.Project.id).all()

def get_proj_details(proj_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if project:
        return project
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')

def create_proj_details(proj: schemas.Project, db: Session):
    try:
        # Check if the project ID already exists
        existing_proj = db.query(models.Project).filter(models.Project.id == proj.id).first()
        if existing_proj:
            raise HTTPException(status_code=400, detail='Project ID already exists')
        
        # Check if the department ID exists
        existing_dept = db.query(models.Department).filter(models.Department.id == proj.dept_id).first()
        if not existing_dept:
            raise HTTPException(status_code=404, detail='No such department found')
        
        existing_proj_name=db.query(models.Project).filter(models.Project.name==proj.name).first()
        if existing_proj_name:
            raise HTTPException(status_code=400, detail='project name already registered')
        
        db_proj = models.Project(**proj.model_dump())
        db.add(db_proj)
        db.commit()
        db.refresh(db_proj)
        return {'message':'project added successfully'}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def update_proj_details(proj_id: int, proj: schemas.Project, db: Session):
    project = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if project:
        project.name = proj.name
        existing_dept = db.query(models.Department).filter(models.Department.id == proj.dept_id).first()
        if not existing_dept:
            raise HTTPException(status_code=404, detail='No such department found')
        project.dept_id = proj.dept_id
        db.commit()
        db.refresh(project)
        return {'message':'project details updated'}
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')

def del_proj_details(proj_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if project:
        db.delete(project)
        db.commit()
        return {'successfully deleted'}
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')