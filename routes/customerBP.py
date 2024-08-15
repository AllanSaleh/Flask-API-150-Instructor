from flask import Blueprint
from controllers.customerController import save, find_all,find_all_paginate, login

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
customer_blueprint.route('/login', methods=['POST'])(login)

## So at this point, when I get logged in, I am not doing anything with the token just yet but I should be able to get a token back and be logged in

## LETS MAKE SURE WE CREATE A CUSTOMER WITH THE USERNAME "Debbie" AND PASSWORD "strongpassword" IN THE DATABASE BEFORE WE TEST THIS OUT BY SENDING A POST REQUEST TO http://localhost:5000/customers WITH THE FOLLOWING JSON PAYLOAD: {"name": "Debbie", "email": "debbie@email.com", "password": "strongpassword", "phone": "123456", "username": "Debbie1212"}
## NOW GO TO POSTMAN AND TEST THIS OUT BY SENDING A POST REQUEST TO http://localhost:5000/customers/login WITH THE FOLLOWING JSON PAYLOAD: {"username": "Debbie", "password": "strongpassword"}


## SO NOW LETS GET INTO ACTUALLY USING THE TOKEN TO VALIDATE THE IDENTITY OF THE USER AND GRANT THEM ACCESS TO CERTAIN ROUTES

    ## So when we are using the token, part of our authorization comes through the header of the request

    ## IN POSTMAN, GO TO THE HEADERS TAB AND you can see that there are no authorization headers set

    ## Postman is nice as it lays out the headers and authorization for you

    ## Gives you nice windows so that when we get into bearer tokens, we can easily set the token in the header and we should see Authorization in our headers

    ## So what this would look like from an api request standpoint, we can see that code through postman code snippets (Python - Requests) (JavaScript - Fetch)

## So knowing what the requests look like and that there's going to be an Authorization header that comes through the request, that's how we actually get the token out of the request

    ## 1. So we have to check if they have an Authorization parameter in the header

    ## 2. Is there a token in the Authorization header

    ## 3. Is it a valid token

## So we will have to go through this process when we are validating the token

## NOW ITS TIME TO START PROTECTING OUR ROUTES AND ONLY ALLOW FOR AUTHORIZED USERS TO ACCESS THOSE ROUTES, IN OTHER WORDS, IMPLEMENTING ACCESS CONTROL

    ## Controlling the flow of access to each one of our routes

## So lets say you can see the products of my ecommerce store but you can't see the orders or make orders until you have a token

## GO TO THE MARKDOWN FILE AND READ IMPLEMENTING ACCESS CONTROL