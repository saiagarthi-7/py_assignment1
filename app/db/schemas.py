from pydantic import BaseModel,field_validator
class Employee(BaseModel):
    id:int
    name:str
    email:str
    position:str
    salary:int
    
    @field_validator('name','email')
    def empty_name_email(cls, name, email):
        if name=='' or email=='':
            raise ValueError('name or email is empty')
        return name
    
    @field_validator('salary')
    def salary_check(cls,salary):
        if salary<0:
            raise ValueError('salary should greater than zero')
        return salary
    
    @field_validator('id')
    def id_check(cls,id):
        if id<0:
            raise ValueError('employee id not to be negative')
        return id
