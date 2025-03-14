from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from db.database import get_db
from services.salary_service import get_salary_details, update_salary_details, del_salary_details
from db.schemas import Salary

router = APIRouter(prefix="/salary", tags=["salary"])

@router.get("/{employee_id}")
async def get_salary(employee_id: int, db: Session = Depends(get_db)):
    return get_salary_details(employee_id, db)

# @router.post("/create")
# async def create_salary(salary: Salary, db: Session = Depends(get_db)):
#     return create_salary_details(salary, db)

@router.put("/update/{employee_id}")
async def update_salary(employee_id: int, salary: Salary, db: Session = Depends(get_db)):
    return update_salary_details(employee_id, salary, db)

# @router.delete("/delete/{employee_id}")
# async def delete_salary(employee_id: int, db: Session = Depends(get_db)): #Depends(get_db) is dependency injection 
    # return del_salary_details(employee_id, db)