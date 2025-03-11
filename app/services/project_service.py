from fastapi import HTTPException
from db.schemas import Project

projects_db = {
    1: {"name": "Project Alpha", "dept_id": 1},
    2: {"name": "Project Beta", "dept_id": 2},
    3: {"name": "Project Gamma", "dept_id": 3},
}

def get_proj_details(proj_id: int):
    if proj_id in projects_db:
        return projects_db[proj_id]
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')

def create_proj_details(proj: Project):
    if proj.id not in projects_db:
        projects_db[proj.id] = {
            "name": proj.name,
            "dept_id": proj.dept_id
        }
        return projects_db[proj.id]
    else:
        raise HTTPException(status_code=400, detail='Project already exists')

def update_proj_details(proj_id: int, proj: Project):
    if proj_id in projects_db:
        projects_db[proj_id] = {
            "name": proj.name,
            "dept_id": proj.dept_id
        }
        return projects_db[proj_id]
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')

def del_proj_details(proj_id: int):
    if proj_id in projects_db:
        deleted_project = projects_db.pop(proj_id)
        return deleted_project
    else:
        raise HTTPException(status_code=404, detail='Project ID not found')