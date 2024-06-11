from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.customer_model import Customer
from circuitbreaker import circuit


# Fallback function - executed once the limit has been passed
def fallback_func(customer_data):
    print('The fallback function is being executed')
    return None

# Function to get all of the customers from the db
def find_all(page=1, per_page=10):
    query = db.select(Customer).offset((page-1) * per_page).limit(per_page)
    customers = db.session.execute(query).scalars().all()
    return customers

# Function that will take in a customer id and return than customer or None
def get_customer(customer_id):
    return db.session.get(Customer, customer_id)