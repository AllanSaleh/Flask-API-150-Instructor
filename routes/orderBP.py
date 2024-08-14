from flask import Blueprint
from controllers.orderController import save, find_all, find_by_id, find_by_customer_id,find_by_customer_email


order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/', methods=['GET'])(find_all)
## for this one, we will use a dynamic route to find an order by id
order_blueprint.route('/<int:id>', methods=['GET'])(find_by_id)
order_blueprint.route('/customer/<int:id>', methods=['GET'])(find_by_customer_id)
order_blueprint.route('/customer/email', methods=['POST'])(find_by_customer_email)

## so whenever this route gets triggered, it will specifically grabbing a single order by id
## the controller will then call the service to get the order by id, the service will then query the database to get the order by id and return it to the controller, the controller will then return the order to the frontend user
## GO TO POSTMAN AND TEST THIS OUT BY SENDING A GET REQUEST TO http://localhost:5000/orders/1


## NOW GO TO ORDERSERVICE.PY FILE TO FIND ORDERS BY CUSTOMER ID


## GO TO POSTMAN AND TEST THIS OUT BY SENDING A GET REQUEST TO http://localhost:5000/orders/customer/1


## NOW GO TO ORDERSERVICE.PY FILE TO START THE SEARCHING FOR ORDERS BY CUSTOMER NAME
## THIS ONE IS ACTUALLY GOING TO REQUIRE A JOIN BECAUSE WE ARE TRYING TRYING TO SEE ALL OF THE ORDERS BUT WE ARE USING AN ATTRIBUTE FROM A DIFFERENT TABLE


## GO TO POSTMAN AND TEST THIS OUT BY SENDING A POST REQUEST TO http://localhost:5000/orders/customer/email AND IN THE BODY, SEND A JSON OBJECT WITH THE KEY EMAIL AND THE VALUE OF THE EMAIL YOU WANT TO SEARCH FOR