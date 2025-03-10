from fastapi import FastAPI
from api.routes import employees
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from jose import jwt

app=FastAPI()

app.include_router(employees.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],    #allow which domains can access the fastapi
    allow_credentials=True, #allow the domains based on the 
    allow_methods=['*'],    #allow specific methods like get, put, post, delete
    allow_headers=['*']
)

SECRET_KEY = 'nmljhgfdsdfghu876543ewdfghj'
ALGORITHM = 'HS256'

def create_access_token(subject: str):
    token = jwt.encode({'data' : subject}, SECRET_KEY, algorithm = ALGORITHM)
    return {'access_token' : token}

@app.get('/create-token')
def create_token_api(name : str):
    token = create_access_token(subject = name)
    return token

def decode_token(token: str):
    data = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
    return data

@app.get('/decode-token')
def decode_token_api(token : str):
    data = decode_token(token = token)
    return data

if "__main__" == __name__:
    uvicorn.run(app,port=8090,reload=True)