from flask import Blueprint
from controllers.customerController import save, find_all,find_all_paginate

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)

## GO TO POSTMAN AND TEST THIS OUT BY SENDING A GET REQUEST TO http://localhost:5000/customers/paginate?page=1&per_page=2
