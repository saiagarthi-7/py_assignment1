from pydantic import BaseModel, field_validator
from typing import Optional

class DepartmentSchema(BaseModel):
    id: Optional[int] = None  
    name: str

class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
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

class SalarySchema(BaseModel):
    id: Optional[int] = None
    employee_id: int
    amount: float

    @field_validator('amount')
    def amount_positive(cls, salary):
        if salary < 0:
            raise ValueError('Salary must be greater than zero')
        return salary

    @field_validator('employee_id')
    def employee_id_positive(cls, id):
        if id < 0:
            raise ValueError('Employee ID must be positive')
        return id