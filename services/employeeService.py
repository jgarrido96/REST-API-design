from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.employee_model import Employee
from circuitbreaker import circuit


# Fallback function - executed once the limit has been passed
def fallback_func(employee_data):
    print('The fallback function is being executed')
    return None

# Function to get all of the employees from the db
def find_all(page=1, per_page=10):
    query = db.select(Employee).offset((page-1) * per_page).limit(per_page)
    employees = db.session.execute(query).scalars().all()
    return employees

# Function that will take in a employee id and return than employee or None
def get_employee(employee_id):
    return db.session.get(Employee, employee_id)