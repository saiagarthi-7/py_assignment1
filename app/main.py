from fastapi import FastAPI
from api.routes import employees
import uvicorn

app=FastAPI()

app.include_router(employees.router)

if "__main__" == __name__:
    uvicorn.run(app,port=8090,reload=True)