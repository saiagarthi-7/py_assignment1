from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class Department(Base):
    __tablename__ = 'departments'
    id : Mapped[int] = mapped_column(primary_key = True, index = True)
    name : Mapped[str] = mapped_column(index = True, nullable = False)

class Employee(Base):
    __tablename__ = 'employees'
    id : Mapped[int] = mapped_column(primary_key = True,index = True)
    name : Mapped[str] = mapped_column(index = True, nullable = False)
    email : Mapped[str] = mapped_column(index = True, nullable = False, unique = True)
    position : Mapped[str] = mapped_column(index = True, nullable = False)
    salary : Mapped[int] = mapped_column(index = True, nullable = False)
    dept_id : Mapped[int] = mapped_column(ForeignKey('departments.id'))

class Project(Base):
    __tablename__ = 'projects'
    id : Mapped[int] = mapped_column(primary_key = True, index = True)
    name : Mapped[str] = mapped_column(index = True, nullable = False)

class Salary(Base):
    __tablename__ = 'salaries'
    id : Mapped[int] = mapped_column(primary_key = True, index = True)
    emp_id = Mapped[int] = mapped_column(ForeignKey('employees.id'))
    amount = Mapped[int] = mapped_column(nullable = False)
    month = Mapped[str] = mapped_column(nullable = False)


