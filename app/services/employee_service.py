from fastapi import HTTPException
from sqlalchemy.orm import Session
from db import models, schemas

def get_all_employees(db: Session):
    return db.query(models.Employee).order_by(models.Employee.id).all()

def get_emp_details(emp_id: int, db: Session):  #function to get emp details by id
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()   #query the db 
        if employee:
            return employee
        else:
            raise HTTPException(status_code=404, detail='Employee ID not found') #raise an HTTP 404 error if the employee is not found
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def create_emp_details(emp: schemas.EmployeeCreate, db: Session):
    try:
        # Check if the employee Id already exists
        existing_emp = db.query(models.Employee).filter(models.Employee.id == emp.id).first()
        if existing_emp:
            raise HTTPException(status_code=400, detail='Employee ID already exists')
        
         # Check if the department number exists
        existing_dept = db.query(models.Department).filter(models.Department.id == emp.dept_id).first()
        if not existing_dept:
            raise HTTPException(status_code=404, detail='No such department found')

        exist_email=db.query(models.Employee).filter(models.Employee.email == emp.email).first()#this var checks if same email exists 
        if exist_email:                                                                         #if exists it do not enter another mail address
            raise HTTPException(status_code=400, detail='email already existed please enter new emailID')
        
        db_emp = models.Employee(**emp.model_dump())
        db.add(db_emp)  # add new employee to db
        db.commit()     # commit the transaction
        return {'Message': "Employee Added Successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')

def update_emp_details(emp_id: int, emp: schemas.EmployeeUpdate, db: Session):
    try:
        #check if employe ID exist
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail='Employee ID not found')
        
        #check if the departmet nmbr exists
        existing_dept = db.query(models.Department).filter(models.Department.id == emp.dept_id).first()
        if not existing_dept:
            raise HTTPException(status_code=404, detail='No such department found')
        
        #update employe detials
        employee.name = emp.name
        employee.email = emp.email
        employee.position = emp.position
        employee.salary = emp.salary
        employee.dept_id = emp.dept_id
        db.commit()
        return {'message': 'Employee Updated Successfully'}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')
    
def del_emp_details(emp_id: int, db: Session):
    try:
        # Check if the employee ID exists
        employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail='Employee ID not found')
        
        # Delete the employee
        db.delete(employee)
        db.commit()
        return {'message': 'Employee successfully deleted'}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal Server Error')