from models.schemas.orderSchema import order_schema, orders_schema
from flask import request, jsonify
from marshmallow import ValidationError
from services import orderService
from utils.util import user_token_required

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

def find_by_id(id):
    orders = orderService.find_by_id(id)
    return orders_schema.jsonify(orders), 200

@user_token_required
def find_by_customer_id(id, token_id):
    if id == token_id:
        orders = orderService.find_by_customer_id(id)
    else:
        return jsonify({"messages": "You can't view other peoples orders..."}), 401
    return orders_schema.jsonify(orders), 200

## GO TO POSTMAN AND TRY TO VIEW ANOTHER USERS ORDERS, TEST IT OUT ON THE ENDPOINT http://localhost:5000/orders/customer/1


def find_by_customer_email():
    email = request.json['email']
    orders = orderService.find_by_customer_email(email)
    return orders_schema.jsonify(orders), 200

## GO TO THE ORDERBP.PY ROUTE FILE