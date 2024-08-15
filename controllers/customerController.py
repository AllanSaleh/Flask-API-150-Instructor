from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import admin_required, token_required

def login():
    try:
        ## try to get the username and password from the request payload
        credentials = request.json
        ## We will pass the username and password to the login function in the customerService module to validate the credentials and create a token
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages': 'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages': "Invalid username or password"}), 401

## NOW GO TO THE CUSTOMERBP.PY FILE TO CREATE THE LOGIN ROUTE THAT WILL CALL THIS FUNCTION

def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201

# @cache.cached(timeout=60)
# @token_required
@admin_required
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200
## LETS MAKE A REQUEST TO FIND_ALL WITHOUT A TOKEN AND SEE WHAT HAPPENS
## IN POSTMAN, SEND A GET REQUEST TO http://localhost:5000/customers

## LEST MAKE A REQUEST TO FIND_ALL WITH A WRONG TOKEN AND SEE WHAT HAPPENS

## LETS LOGIN AND GET A TOKEN AND USE THAT TOKEN TO MAKE A REQUEST TO FIND_ALL
@admin_required
def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200


# GO TO THE ROUTES/CUSTOMERBP.PY FILE