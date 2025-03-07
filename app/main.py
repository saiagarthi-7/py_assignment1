from fastapi import FastAPI,HTTPException
from api.routes import employees
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']

)

app.include_router(employees.router)

if "__main__" == __name__:
    uvicorn.run(app,port=8090,reload=True)