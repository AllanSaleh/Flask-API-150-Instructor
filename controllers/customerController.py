from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache


def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200


# GO TO THE ROUTES/CUSTOMERBP.PY FILE