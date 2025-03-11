from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    position = Column(String, index=True, nullable=False)
    salary = Column(Integer, index=True, nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.id'))



class Salary(Base):
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey('employees.id'))
    amount = Column(Integer, nullable=False)
