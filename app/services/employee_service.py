employees_db = {
    1: {"name": "sai", "email": "sai@aifa.com", "position": "Software Engineer", "salary": 75000},
    2: {"name": "ram", "email": "ram@aifa.com", "position": "Manager", "salary": 90000},
    3: {"name": "mohan", "email": "mohan@aifa.com", "position": "Data Scientist", "salary": 85000},
}

def get_emp_details(emp_id):
    if emp_id in employees_db:
        return employees_db[emp_id]
    else:
        return {'no id found'}

def create_emp_details(emp):
    if emp.emp_id not in employees_db:
        employees_db[emp.emp_id] ={}
        employees_db[emp.emp_id]['name']=emp.name
        employees_db[emp.emp_id]['email']=emp.email
        employees_db[emp.emp_id]['position']=emp.position
        employees_db[emp.emp_id]['salary']=emp.salary
        return True
    else:
        return {'message':'already existed'}
    
def update_emp_details(emp_id,name):
    if emp_id in employees_db:
        employees_db[emp_id]['name']=name
        return True
    else:
        return {'id not found'}

def del_emp_details(emp_id):
    if emp_id in employees_db:
        del employees_db[emp_id]
        return {'successfully deleted'}
    else:
        return {'id not found'}