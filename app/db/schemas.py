from pydantic import BaseModel
class Employee(BaseModel):
    emp_id:int
    name:str
    email:str
    position:str
    salary:int