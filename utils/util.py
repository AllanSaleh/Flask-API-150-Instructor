from datetime import datetime, timedelta, timezone ##1
from secrets import token_bytes
import jwt ##1
from flask import jsonify, request #So we can access the request and validate the headers
from functools import wraps #package that will allow us to create wrappers

## this secret key can be anything you want, but it should be a long random string because it will be used to encode and decode the token
SECRET_KEY = "super_secret_secrets"

## Function to generate a random token so that when the user logs in with their credential, we can validate their credentials and give them a token
## we don't need to pass in the user_id here but its good to throw in there to make the token unique and specific to the user
##  So that no 2 users will have the same tokens. There's no chance for it, because every 2 users or all users have different ids.
def encode_token(user_id, role): #using unique pieces of info to make our tokens user specific
    ## payload is the data we want to store in the token and we can access it later
    ## we can store the user_id, role, and expiration time
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0,hours=1), #Setting the expiration time to an hour past now
        'iat': datetime.now(timezone.utc), #Issued at
        'sub': user_id, #Sub stands for subject aka who the token is for
        'role': role ##2
    }

    ## now we encode the payload with our secret key and the algorithm we want to use
    ## it will use the secret key to do what is called signing the token
    ## this will make sure that the token is valid and hasn't been tampered with
    ## it depends on the secret key to morphe the token into something that can be decoded later
    ## to undo this signing and decode the token, we need the secret key
    ## the algorithm is the type of encryption we want to use, it is an hashing algorithm
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

## Now we should create a login function that will take in the user's credentials and validate them
## login is one of main ways that we should give out tokens
## if they login successfully, we will give them a token
## token will be used to validate their identity and role and grant them access to certain routes

## SO LETS CREATE OUR LOGIN ROUTE, SO WE WILL START FROM OUR SERVICE -> CONTROLLER -> ROUTE
## SO LETS GO TO OUR CUSTOMER SERVICE AND CREATE A LOGIN FUNCTION


## Creating the wrapper is going to look funny as we have never created a wrapper before so its something we are not super familiar with
## For the wrapper to have access to the request object to check if the token is in the header, we will import jsonify and request from flask
## We will also import wraps from functools to create our wrapper

#creating our wrapper
def token_required(func): #Finds func based on what function the wrapper is sitting on
    @wraps(func) ## this helps the wrapper fund the function that it is wrapping
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1] #Separating "Bearer <token>" into ["Bearer", <token>], and grabbing <token>
                ## when we decode the token, we are going to check if the token is expired or invalid
                ## payload is the data that we stored in the token that we get back when we decode the token so if I need the user_id or role, I can get it from the payload
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            return func(*args, **kwargs) #Executing the function we are wrapping if, the token is validated
        else:
            return jsonify({"messages": "Token Authorization Required"}), 401
    return wrapper

## GO TO OUR CUSTOMERCONTROLLER.PY AND ADD @TOKEN_REQUIRED TO THE FIND_ALL FUNCTION


## user_token_required wrapper will be to for the example of trying to see other users orders
def user_token_required(func): #Finds func based on what function the wrapper is sitting on
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1] #Separating "Bearer <token>" into ["Bearer", <token>], and grabbing <token>
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            return func(token_id=payload['sub'],*args, **kwargs) #Executing the function we are wrapping if, the token is validated
        else:
            return jsonify({"messages": "Token Authorization Required"}), 401
    return wrapper
## GO TO OUR ORDERCONTROLLER.PY AND ADD @USER_TOKEN_REQUIRED TO THE FIND_BY_CUSTOMER_ID FUNCTION

def admin_required(func): #Finds func based on what function the wrapper is sitting on
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split()[1] #Separating "Bearer <token>" into ["Bearer", <token>], and grabbing <token>
                payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                print("Payload:", payload)
            
            except jwt.ExpiredSignatureError:
                return jsonify({'message': "Token has expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401
            if payload['role'] == "Admin":
                return func(*args, **kwargs) #Executing the function we are wrapping if, the token is validated
            else:
                return jsonify({"messages": "Admin role required"}), 401
        else:
            return jsonify({"messages": "Token Authorization Required"}), 401
    return wrapper

