from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from db import crud, schemas
from api.routes.configuration import settings
from api.routes.security import create_access_token
from db.crud import get_current_employee
from db.database import get_db

oauth = OAuth2PasswordBearer(tokenUrl="authorize/token")

router = APIRouter(prefix="/authorize", tags=["authorize"])

@router.post("/token", response_model=schemas.Tokens)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=user.username, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/Employees", response_model=schemas.Employee)
def read_users_me(current_user: schemas.Employee = Depends(get_current_employee)):
    return current_user