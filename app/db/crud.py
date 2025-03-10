from sqlalchemy.orm import Session
import models
import schemas

# DEPARTMENT
def create_department(db: Session, dept: schemas.DepartmentCreate):
    db_dept = models.Department(**dept.dict())
    db.add(db_dept)
    db.commit()
    return db_dept

def get_department(db: Session):
    return db.query(models.Department).all()

# EMPLOYEE
def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    return db_emp

def get_employee(db: Session):
    return db.query(models.Employee).all()

# PROJECT
def create_project(db: Session, proj: schemas.ProjectCreate):
    db_proj = models.Project(**proj.dict())
    db.add(db_proj)
    db.commit()
    return db_proj

def get_project(db: Session):
    return db.query(models.Project).all()

# SALARY
def create_salary(db: Session, salary: schemas.SalaryCreate):
    db_salary = models.Salary(**salary.dict())
    db.add(db_salary)
    db.commit()
    return db_salary

def get_salary(db: Session):
    return db.query(models.Salary).all()
