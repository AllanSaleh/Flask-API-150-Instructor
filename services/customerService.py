from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select
from utils.util import encode_token

def login(username, password): #Login using unique info so we dont query multiple users
    query =select(Customer).where(Customer.username == username)  
    customer = db.session.execute(query).scalar_one_or_none() #Query customer table for a cuastomer with the passwed in username

    if customer and customer.password == password: #if we have a customer associated with the username, validate the password
        auth_token = encode_token(customer.id, customer.role.role_name)
        # auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": auth_token
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "Invalid username or password"
        }
        return response

## NOW GO TO CUSTOMERCONTROLLER.PY FILE TO CREATE THE LOGIN FUNCTION THAT WILL CALL THIS FUNCTION

def save(customer_data):
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], password=customer_data['password'], phone=customer_data['phone'], username=customer_data['username'])
    db.session.add(new_customer)
    db.session.commit()

    db.session.refresh(new_customer)
    return new_customer

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    customers = db.paginate(select(Customer), page=page, per_page=per_page)
    return customers

## GO TO THE CUSTOMERCONTROLLER.PY FILE