from fastapi import Depends, APIRouter
from db.database import get_db
from sqlalchemy.orm import Session
from services.project_service import get_all_projects, get_proj_details, create_proj_details, update_proj_details, del_proj_details
from db.schemas import Project

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/")
async def get_projects(db: Session = Depends(get_db)):
    projects = get_all_projects(db)
    return projects

@router.get("/{project_id}")
async def get_project(project_id: int, db: Session = Depends(get_db)):
    project = get_proj_details(project_id, db)
    return project

@router.post("/create")
async def create_project(project: Project, db: Session = Depends(get_db)):
    new_project = create_proj_details(project, db)
    return new_project

@router.put("/update/{project_id}")
async def update_project(project_id: int, project: Project, db: Session = Depends(get_db)):
    updated_project = update_proj_details(project_id, project, db)
    return updated_project

@router.delete("/delete/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted_project = del_proj_details(project_id, db)
    return deleted_project
