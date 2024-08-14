from flask import Blueprint
from controllers.productController import find_all, save, search_product


product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)

product_blueprint.route('/search', methods=['GET'])(search_product)
## so a frontend user like postman, it hits the endpoint /search?search=product_name that triggers the search_product function in the controller layer to trigger a query based on the search term and communicates with the database to return the search results back to the controller layer and then back to the frontend user

## So now we should have a new endpoint that allows us to search for products by name.

## lets test it in postman by sending a GET request to http://localhost:5000/products/search?search=lotion and we should get a response with the product that has the name product_name

## We now have our search functionality in place. So a frontend user can now search for products by name. They can create different links so that they can query based off of the search term

## So based on this functionality, a frontend user can make a dynamic search bar that allows as the user types in the search bar, the search results are updated in real time. This is a very common feature in many websites and applications. This is what we are allowing the frontend user to do with our search functionality.

## It's a collaborative effort between the frontend and backend to make this happen. The frontend user can make a request to the backend to get the search results and the backend can query the database to get the search results and return them to the frontend user. This is how the search functionality works in a web application.

