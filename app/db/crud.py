from sqlalchemy.orm import Session
import models
import schemas

# -------------- DEPARTMENT ------------
def create_department(db: Session, dept: schemas.Department):
    db_dept = models.Department(**dept.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def get_departments(db: Session):
    return db.query(models.Department).all()

def update_department(db: Session, dept_id: int, dept: schemas.Department):
    db_dept = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if db_dept:
        for key, value in dept.dict().items():
            setattr(db_dept, key, value)
        db.commit()
        db.refresh(db_dept)
    return db_dept

def delete_department(db: Session, dept_id: int):
    db_dept = db.query(models.Department).filter(models.Department.id == dept_id).first()
    if db_dept:
        db.delete(db_dept)
        db.commit()
    return db_dept

# -------------- EMPLOYEE ---------------
def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def get_employees(db: Session):
    return db.query(models.Employee).all()

def update_employee(db: Session, emp_id: int, emp: schemas.EmployeeCreate):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_emp:
        for key, value in emp.dict().items():
            setattr(db_emp, key, value)
        db.commit()
        db.refresh(db_emp)
    return db_emp

def delete_employee(db: Session, emp_id: int):
    db_emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_emp:
        db.delete(db_emp)
        db.commit()
    return db_emp

# --------------- PROJECT ---------------
def create_project(db: Session, proj: schemas.Project):
    db_proj = models.Project(**proj.dict())
    db.add(db_proj)
    db.commit()
    db.refresh(db_proj)
    return db_proj

def get_projects(db: Session):
    return db.query(models.Project).all()

def update_project(db: Session, proj_id: int, proj: schemas.Project):
    db_proj = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if db_proj:
        for key, value in proj.dict().items():
            setattr(db_proj, key, value)
        db.commit()
        db.refresh(db_proj)
    return db_proj

def delete_project(db: Session, proj_id: int):
    db_proj = db.query(models.Project).filter(models.Project.id == proj_id).first()
    if db_proj:
        db.delete(db_proj)
        db.commit()
    return db_proj

# --------------- SALARY ---------------
def create_salary(db: Session, salary: schemas.Salary):
    db_salary = models.Salary(**salary.dict())
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)
    return db_salary

def get_salaries(db: Session):
    return db.query(models.Salary).all()

def update_salary(db: Session, salary_id: int, salary: schemas.Salary):
    db_salary = db.query(models.Salary).filter(models.Salary.id == salary_id).first()
    if db_salary:
        for key, value in salary.dict().items():
            setattr(db_salary, key, value)
        db.commit()
        db.refresh(db_salary)
    return db_salary

def delete_salary(db: Session, salary_id: int):
    db_salary = db.query(models.Salary).filter(models.Salary.id == salary_id).first()
    if db_salary:
        db.delete(db_salary)
        db.commit()
    return db_salary
