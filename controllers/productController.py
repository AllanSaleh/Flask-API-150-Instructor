from flask import jsonify, request
from models.schemas.productSchema import product_schema,products_schema
from marshmallow import ValidationError
from services import productService

def save():
    try:        
        # Validate and deserialize input
        product_data = product_schema.load(request.json)
    except ValidationError as err:
            return jsonify(err.messages), 400    
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 200

## this is where the return from the service is received and returned to the client, more specifically the return of the search_product function in the service layer

## request.args.get("search") is used to get the value of the search query parameter from the URL in the request object and assign it to the search_term variable
def search_product():
     search_term = request.args.get("search")
     searched_items = productService.search_product(search_term)
     return products_schema.jsonify(searched_items)

## Now what triggers my controller to run? Answer: The routes.py file so lets go to productBP.py