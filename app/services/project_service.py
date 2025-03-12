from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas, database

def get_all_projects(db: Session):
    return db.query(models.Project).all()

def get_proj_details(proj_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if project:
        return project
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')

def create_proj_details(proj: schemas.Project, db: Session):
    db_proj = models.Project(**proj.model_dump())
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

def update_proj_details(proj_id: int, proj: schemas.Project, db: Session):
    project = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if project:
        project.name = proj.name
        project.dept_id = proj.dept_id
        db.commit()
        db.refresh(project)
        return project
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