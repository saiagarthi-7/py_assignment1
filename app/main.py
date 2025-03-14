from fastapi import FastAPI
from api.routes import employees, projects, department, salary, authorize
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db.database import engine
from db import models
from jose import jwt
from api.routes.security import create_access_token, decode_token

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management System")

app.include_router(employees.router)
app.include_router(projects.router)
app.include_router(department.router)
app.include_router(salary.router)
app.include_router(authorize.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],    # allow which domains can access the fastapi
    allow_credentials=True, # allow the domains based on the 
    allow_methods=['*'],    # allow specific methods like get, put, post, delete
    allow_headers=['*']
)

@app.get('/create-token')
def create_token_api(name: str):
    try:
        token = create_access_token(subject=name)
        return token
    except Exception as e:
        return {"error": e}

@app.get('/decode-token')
def decode_token_api(token: str):
    try:
        data = decode_token(token=token)
        return data
    except Exception as e:
        return {"error": e}

if __name__ == "__main__":
    uvicorn.run(app, port=8090, reload=True)