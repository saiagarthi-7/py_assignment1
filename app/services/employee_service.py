from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_all_employees(db: Session):
    return db.query(models.Employee).all()

def get_emp_details(emp_id: int, db: Session):  #function to get emp details by id
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()   #query the db 
        if employee:
            return employee
        else:
            raise HTTPException(status_code=404, detail='Employee ID not found') #raise an HTTP 404 error if the employee is not found
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def create_emp_details(emp: schemas.EmployeeCreate, db: Session):
    try:
        db_emp = models.Employee(**emp.model_dump())
        db.add(db_emp)  #add new employee to db
        db.commit()     #commit the transaction
        return {'Message':"Employee Added Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def update_emp_details(emp_id: int, emp: schemas.EmployeeUpdate, db: Session):
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
        if employee:
            employee.id=emp.id
            employee.name = emp.name
            employee.email = emp.email
            employee.position = emp.position
            employee.salary = emp.salary
            db.commit()
            return {'message':'Updated'}
        else:
            raise HTTPException(status_code=404, detail='Employee ID not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def del_emp_details(emp_id: int, db: Session):
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
        if employee:
            db.delete(employee)
            db.commit()
            return {'successfully deleted'}
        else:
            raise HTTPException(status_code=404, detail='Employee ID not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')