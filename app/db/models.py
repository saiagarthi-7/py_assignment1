from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    age = Column(Integer, index=True)
    email = Column(String, index=True, nullable=False)
    hashed_password= Column(String, nullable=False)
    position = Column(String,index=True, nullable=False)
    salary = Column(Float, index=True, nullable=False)
    dept_id = Column(Integer, ForeignKey("departments.id"))


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))


class Salary(Base):
    __tablename__ = 'salaries'
    emp_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    amount = Column(Float)
