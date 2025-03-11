from fastapi import APIRouter, HTTPException
from typing import List
from db.schemas import Project
from services.project_service import projects_db, create_proj_details, update_proj_details, del_proj_details, get_proj_details

router = APIRouter(prefix="/projects", tags=['projects'])

@router.get("/")
async def get_projects():
    return projects_db

@router.get("/{project_id}")
async def get_project(project_id: int):
    project = get_proj_details(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/")
async def create_project(project: Project):
    new_project = create_proj_details(project)
    return new_project

@router.put("/{project_id}")
async def update_project(project_id: int, project: Project):
    updated_project = update_proj_details(project_id, project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@router.delete("/{project_id}")
async def delete_project(project_id: int):
    deleted_project = del_proj_details(project_id)
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return deleted_project