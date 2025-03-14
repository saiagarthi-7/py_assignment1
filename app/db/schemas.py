from pydantic import BaseModel, field_validator
from typing import Optional

class Department(BaseModel):
    id: int  
    name: str

class DepartmentUpdate(Department):
    name: str

    @field_validator('name')
    def name_not_empty(cls, name):
        if not name:
            raise ValueError('Name cannot be empty')
        return name

class Employee(BaseModel):
    id: int
    name: str
    age: int  
    email: str
    position: str
    salary: int
    dept_id: int

    @field_validator('name')
    def name_not_empty(cls, name):
        if not name:
            raise ValueError('Name cannot be empty')
        return name

    @field_validator('age')
    def age_positive(cls, age):
        if age < 0:
            raise ValueError('Age must be positive')
        return age

    @field_validator('dept_id')
    def dept_id_positive(cls, id):
        if id < 0:
            raise ValueError('Department ID must be positive')
        return id
    
class EmployeeCreate(Employee):
    pass

class EmployeeUpdate(BaseModel):
    name: str
    age: int  
    email: str
    position: str
    salary: int
    dept_id: int

class Project(BaseModel):
    id: Optional[int] = None
    name: str
    dept_id: int

    @field_validator('name')
    def name_not_empty(cls, name):
        if not name:
            raise ValueError('Name cannot be empty')
        return name

    @field_validator('dept_id')
    def dept_id_positive(cls, id):
        if id < 0:
            raise ValueError('Department ID must be positive')
        return id

class Salary(BaseModel):
    amount: float

    @field_validator('amount')
    def amount_positive(cls, salary):
        if salary < 0:
            raise ValueError('Salary must be greater than zero')
        return salary
class SalaryUpdate(BaseModel):
    amount: float

    @field_validator('amount')
    def amount_positive(cls, salary):
        if salary < 0:
            raise ValueError('Salary must be greater than zero')
        return salary
    
class Tokens(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class EmployeeLogin(BaseModel):
    username: str
    password: str