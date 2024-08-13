## Learning Objectives

- Students should be able to design REST APIs using best practices for resource naming, endpoint structuring, and efficient patterns, ensuring scalability and maintainability.
- Students should be able to apply modularization in REST APIs and demonstrate how to apply it effectively to improve code maintainability, reusability, and scalability.
- Students should be able to understand the concept of caching and how to apply it in REST APIs to improve performance and efficiency.
- Students should be able to grasp the significance of setting rate limits in REST APIs and how to apply rate-limiting strategies to ensure fair and sustainable use of server resources.


- `in terms of rest. Apis, we've already dipped our toes into what a rest Api is, but what we did in the end of backend core was. We just kind of cobbled it all together on one single page. Which works. But it's sloppy. There's a lot of moving parts all in one single spot and it gets really untidy, really fast. And it's kind of hard to see at a glance what the Api even does and what it can accomplish.`
- `So this factory application pattern that we're going to be applying today is really used for`
1. `This whole idea of, you know, maintainability, reusability and scalability. So it allows us to kind of add and take things away pretty efficiently.`
2. `It'll really just help us with understanding. Okay, what does this API even do? What are the key parts of it? And how can I use it?`
- `And then also really just being able to And then also really just being able to again modularize this thing. Make it easy to kind of manipulate is kind of what we're going to be setting up, and it's honestly not hard to set up`
- `slotting different. What we call blueprints in might feel a little bit tedious, but once you get a blueprint in adding the routes to that blueprint become much easier.`
- `and then, if you ever don't want that blueprint in there anymore, you could just unplug it essentially.`

#### Recap
`But first, st let's just do a recap on naming convention in terms of how we should be naming our routes to follow this kind of idea of rest. Api.`

##### Naming Convention:
- Use Plural Nouns for resource names
`These shouldn't be adjectives. They shouldn't be anything wild.`
```python
/products
/customers
/orders
```
Use plural even when accessing single items of a collection
```python
/products/{id}
```
- Hyphens to separate words
`you can also use under scores but don't use spaces here, even the %20 you really dont want to use that here either`
```python
/product-categories
```
- Always lowercase
- Use Query parameters for filtering, sorting, and pagination (NEW)
`/products?category=electronics` (query params start after a question mark)
`/products?sort=price` (param=value)
`/products?limit=10&offset=20` (Multiple params separated by &)
- `query, parameters are just a quick way to get information from the URL into your route without having to do anything crazy like. Look up item Ids, or send a whole post request to get information from point A to Point B. send a whole post request to get information from point A to Point B.`
- `By slotting in a query param, we can easily get small bits of information out of our URL to then throw into our API`

### Advanced API Patterns

So far we've been able to create a full api all on a single document, while we can continue to do so this format lends itself to becoming cumbersome and difficult to maintain as the api gets more complex. This is why we turn to the `Factory Aplication Pattern`
- `So far we've been able to create full Apis on a single document which have been great. They've worked but they're gross, right? And
as we kind of expand things, yes, we can continue to just pile garbage on top of garbage and make just the longest one sheeter Api out there, and it'll work until it doesn't, and whether or not it gets updated or whatever happens to it, it'll be very hard to figure out how it's broken, where it's broken, why, it's broken, and how to fix it.And if I when I go to fix it, when it's all kind of jumbled in there together. When I make that one change here, how is that going to cascade and affect the rest of my API, Answer could be substantially.`

##### Factory Aplication Pattern:
Allows for a more dynamic and scaleable API because it allows us to break our api into sub-units called blueprint,
- `A blueprint will house all of the routes for category of capabilities. So we might have a customer's blueprint which handles everything to do with a customer, such as creating customers, logging in customers, logging out customers, retrieving customers, deleting customers, anything to do with our customers might end up in a customer's blueprint. things to do with orders would end up in orders, blueprint, things to do with products will be in products blueprint, so on and so forth.`
- `what's nice is, if we ever wanted to change, modify, or take out anything to do with like a major category. We can just take that thing off like we can unplug it or do what's called unregister that blueprint. So it's no longer affecting our Api`
    - `this is what becomes very powerful in terms of continuous development. So as we want to update things ourselves as we want to change, things comes easy to take one piece out and put another in without really having too many effects on the rest of your application, which is pretty cool.`
each responsible for a different capabilities, we then configure our API with these desired blueprints, allowing us to slot in and take off blueprints at will.

The overall file structure of an API broken into a Factory Application will look something like this.
- `essentially, we're going to break apart what we did. and backend core for that one like one pager API, we're going to break it apart into these different portions, and once it's isolated to these different portions, we're going to be able to do more things with it, such as rate limiting and caching.`
- `Not that you can't do those things on a 1 page Api, but comes easier to kind of control things in this way. And this is more industry standard.`
    - `If you ever look at diagrams which we will actually see one of the diagrams that I grabbed. Every single one of the diagrams that kind of represents what an Api should do. Goes from the user who's making the request goes into routing, which is going to be our route, which goes into our controller, then our model, which is going to be our services, which actually serves the data to our database gets the response, sends it back to the controller, and the controller will respond back to the user with some kind of response message or with a payload of itself.`
```
Project folder
├── app.py
├── config.py
├── database.py
├── controllers
│   ├── __init__.py
├── models
│   ├── __init__.py
│   └── schemas
│       ├── __init__.py
├── requirements.txt
├── routes
│   ├── __init__.py
└── services
    ├── __init__.py
```
`so that is kind of the outline for today. we're gonna have pretty much all of these files and folders set up by the end of the day. And then some because we're gonna have things in our models. We're gonna have things in controllers, routes and all that. Good stuff.`
#### `So let's get started. `
`You guys are welcome to follow along if you want. but because we're covering so many things today, if you guys get stuck. I'm going to say this now. I will not be stopping just because if we stop for every single issue. There's a chance we don't finish today. So and you'll have access to this. This will be used for your homework. so I'll make sure that you guys have a working copy. So even if you're following along and you get stuck somewhere, you will have, you know, minds to fall back on if you need it. So I'm making this disclaimer. Now, please don't say Hey, mine's not working, because I don't want to have to say, well, sorry that sucks that sucks to say but I also don't, wanna you know, get caught up in that alright.`
### `## Go to Notebook`
###### Today's Required packages
requirements.txt
```
Flask
Flask-SQLAlchemy
flask_marshmallow
marshmallow-sqlalchemy
mysql-connector-python
```
`pip install -r requirements.txt` To install these packages from the above page

#### General Flow
- **Create Config file (config.py)**: The config file is responsible for configuring the  the attributes of your flask API (database URI string: 'mysql+mysqlconnector://root:password@localhost/database')
- `Our config.py is really just the folder that is going to configure our app. so nothing too crazy with it.`
- `The main things that are going to be involved in our config.py are going to be our database Uri. So how are we connecting to our database And some other things like Debug? And later on we'll talk about our caching.`
- `config.py. Will holds multiple different configurations for our Api we will have one for development as well as one for deployment. So you know, depending on whether or not we're trying to deploy or develop our app, we will have different configs for it. So for right now, because we haven't really done anything. we're definitely going to be in development mode.`
```python
## IN CONFIG.PY
## need to jump to MySQL to create a connection so that I can create this URI
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/database'
```
- `create a config.py file and write the above line of code`
- `open up mysql workbench and create a new connection with the name bes_ecom`
- `Write the following in the workbench and press execute(thunder icon):`
```sql
CREATE DATABASE bes_ecom;

USE bes_ecom;
```
- `Go to config.py and replace the password with your password (rootuser) and the database name to the database name (bes_com)`
- `Also because we are in development, we'll turn our debugger on`
```python
## IN CONFIG.PY
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:rootuser@localhost/bes_ecom'
    DEBUG = True
```


- **Create Database file (database.py)**: This file is responsible for configuring and initializing our SQLAlchemy database.
- `in this database file, this is just where we're going to set up:`
    - `Our DB, we're going to instantiate SQL alchemy and create our DB.`
    - `we're also going to make that base model, so that when we go to create models for our database, they have some inherited properties from this base model that we're about to create.`
 
# `One thing I forgot`
- `One thing I actually forgot, and I forgot to put it in our notes is, we'll also actually have our schema. schema.py.`
- `Schema doesn't need its own file, and it eventually will not have its own file.`
- `But we need it for now`
#### `Create schema.py and write:`
```python
from flask_marshmallow import Marshmallow

ma = Marshmallow()
```

## `In our app.py`
- `So we're gonna have to import a couple different things for starter.`
- `This is where we're actually going to instantiate flask.`
- `This is where we're also going to add in and initialize/configure our database to work on our app.`
- ` then from Schema, That should be schemas. It doesn't really matter right now, because we will change it`
- `Config will come into play here in just a second. But we're gonna do something cool to add it in here. Not just import it directly.`

```python
from flask import Flask
from database import db
from schema import ma
```

- **Create our Application Factory (app.py)**: Here we create a function that will initialize our Flask App, configure the app using our config file, connect our app to our db, and also lay the ground work for our app schemas

- `So we have this set up the next thing we want to do is actually create what is called our application factory. And that's really just a function that's going to instantiate and initialize everything for our app. So we will be modifying our factory quite a bit as we progress through today.`
- `But for now, it's going to be pretty simple.` 
- `So def create app and then we're gonna use our config name. So whatever configuration we're using, whatever config from our config file we want to use again.`
- `We will eventually have something like a deployment config, our development config.` 
- `we potentially will have more than just one config. So we want to be able to kind of slot them in and out as we see fit.`
- `Right up here at the top is where we're going to instantiate our flask app`
```python
app = Flask(__name__)
```
- `This is where we're going to go ahead and configure our app. this is where we're actually going to create object. And then this is where we're actually going to create the path to our specified config file.`
- `So we're going to go to config. And that's kind of meaning this config file dot whatever config name we pass in here.`
- `this is going to do is it's going to allow me to create this app with either my development config, or later on with my deployment config.`
```python
app.config.from_object(f'config.{config_name}')
```
- `adding the dB to our app, really so initializing our database on our app.`
```python
db.init_app(app)
```
- `and we're going to be doing this with pretty much everything we set up today. and then later we'll be adding our cache as well as our limiter here as well`
```python
from flask import Flask
from database import db
from schema import ma

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    print('Running')
    return app
```
- `Lets setup our run command`
```python
if __name__ == '__main__':
    ## it'll use the proper config from my config file.
    app = create_app('DevelopmentConfig')

    app.run()
```
- `We've kind of separated some concerns which will be super beneficial if we do ever, turn this into a beast of an Api. We'll be able to change up our configurations. change up our database if we need to.`
- `So from here I'm going to give it a test run. Make sure everything is plugged in correctly.`

#### Creating Blueprints

 
## Introduction to Blueprints
- `Now for the fun part. So now that we have this application factory set up, it's pretty much ready for us to start plugging in blueprints.`
- `But blueprints are maybe a little bit more cumbersome than they might originally sound.`
- `There are... Let’s look at my little diagram.`
- `There are technically, five parts`

## Blueprints Overview
- `We have the routing. So that will be our blueprint route.`
- `We’ll create controllers, which are essentially what validates, deserializes, and re-serializes all the information coming in and going out of our API.`
- `We will have what we call a service, which is what serves information directly to and from our database.`
- `But from here, we also need to create our models, so kind of our database tables which we’re familiar with, as well as the accompanying schemas.`
- `So that we can validate what the information for a particular table should look like, which is what our schemas are going to help us do.`

## Starting with Models
- `Alright, so let’s go ahead and start off with our models. So we’re going to start with the models folder.`

## Starting with Blueprints
- `we’ll start with initializing our blueprint, just so we kind of know what we’re working towards.`
- `So blueprints will actually be located in a routes folder.`
- `Inside this routes folder, and I want to make sure that we're following along here, we do want to put these __init__.py files right here.`
- `What a __init__.py inside of a folder does for us in Python is it allows us to treat the folder itself as a file.`
- `So we can write inside of this __init__.py file, and whenever we reference the folder itself, we can reference it as if it were a file.`
- `This becomes really important when we’re importing different things from other folders as a module, and we’ll see that here in a bit.`


## Creating the `__init__.py` File in routes folder
- `Let me go ahead and create my __init__.py. And I'm not even going to write anything in it.`
- `This is strictly so that I can treat this routes folder as a file.`
- `But yeah, for right now, we're going to kind of leave this as is, and then we’re going to get right into actually creating our first blueprint.`

## Creating the Customer Blueprint
- `So, create customerBP.py. in routes`
- `Once we’re in one of our blueprints, this is where we can actually start to create our blueprint.`
- `Alright, from Flask—we don’t have our controllers just yet, so we’ll actually leave it like that for now.`
- `And we’ll actually go ahead and create this blueprint. So customer_blueprint = Blueprint('customer_bp', __name__).`
- `And that’s this blueprint pretty much ready. Obviously, we haven’t done anything with this blueprint yet; we haven’t added any routes to it yet.`
- `So it’s kind of useless at this point, but we will start to fill this blueprint in with some routes.`
- `Those routes are going to depend on controllers. Those controllers are going to depend on some services. Those services are going to depend on models. So we’re going to start with models and kind of work our way back to our blueprints over here.`
```python
from flask import Blueprint
from controllers.customerController import save, find_all

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
```
## Creating the Customer Model
- `Alright, so getting into it, we’re going to create our model.`
- `Again, let me go ahead and create a __init__.py right here. And do make sure that it is a double underscore.`
- `I’ve had people put single underscores, and because of that, it doesn’t work.`
- `You’re not able to path into this file the way you would expect to, and finding a single underscore versus a double underscore can be very tricky.`
- `Alright, so please don’t make that mistake, or else we’ll have to pull out our magnifying glasses for that. So make sure it is a __init__.py.`

## Writing the Customer Model
- `Alright, let's go ahead and create our customer.py model.`
- `First and foremost, from database, we need to import both our db that we created as well as our BaseModel that we created.`
- `We will also want to go ahead and import from sqlalchemy.orm.`
- `We want to grab mapped, as well as mapped_column, collection_column which you guys are probably familiar with. We need these to create our table.`
- `Class Customer is going to take in our BaseModel class that we created, so it's going to inherit those features.`
- `Really, what it’s allowing us to inherit is the ability to use mapped and mapped_column. That’s why we create this base class to begin with, so that we can use these features here.`
```python
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
```

we'll learn how to create a model to interact with our database using our ORM. We'll be focusing on setting up a customer model with various attributes:

1. Define the Model We're starting by creating a model named Customer.

```python
class Customer(db.Model):
    __tablename__ = 'customers'
```
2. Add Attributes
Next, we'll define the attributes for our Customer table. These attributes will become the columns in the database table.

```python
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
```
3. Key Points
ID: The id field is the primary key.
```python
id = db.Column(db.Integer, primary_key=True)
```
Name, Phone Number, Email, Username, Password: These fields are of type String with a maximum length defined. They are all set to nullable=False to ensure these fields are required.
```python
name = db.Column(db.String(255), nullable=False)
phone_number = db.Column(db.String(20), nullable=False)
email = db.Column(db.String(255), unique=True, nullable=False)
username = db.Column(db.String(255), unique=True, nullable=False)
password = db.Column(db.String(255), nullable=False)
```
4. Unique Constraints
Email and Username: These fields are unique to prevent duplicate entries.
```python
email = db.Column(db.String(255), unique=True, nullable=False)
username = db.Column(db.String(255), unique=True, nullable=False)
```
4.5  ` Import the Customer table into the app.py file`
```python
from models.customer import Customer
```


5. Creating Schemas
`Copy the code in the schema.py file from the outside and paste it in the new schemas file in the models folder`
```python
from models.customer import Customer
```
Schemas help with validation of incoming and outgoing data. They ensure the data is controlled and consistent.

```python
from flask_marshmallow import Marshmallow

ma = Marshmallow()
```
6. Incorporate Schemas
Schemas can be placed in the schemas folder. Ensure that the schemas are referenced correctly in your application.

```python
# Import the schema
from models.schemas import CustomerSchema
```
7. Conclusion
We have set up the model and schemas. This is a foundational step in interacting with your database.

So let's go ahead and start creating some schemas. We're going to create our customer schema now inside models/schemas.customerSchema.py"

2. **Purpose of Schema**

   "Remember, the schema is really to help us with the validation of incoming as well as outgoing data. We want to make sure that when we're sending out information, we're doing it in a controlled way."

3. **Importing Dependencies**

   ```python
   from . import ma
   from marshmallow import fields
   ```
"We want to grab that ma thing, which is the Marshmallow instantiation. So we're importing ma from the schemas folder and fields from Marshmallow."

Setting Up the Schema

"To set up this schema, we'll create a new class called CustomerSchema that inherits from ma.Schema."

Lets split the screen the customerSchema.py and the customer.py model file

```python
class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String()
    username = fields.String()
    password = fields.String()
```
### ID Field

"The id field is an integer and is not required because a user won't have an ID when signing up, as it will be auto-generated."

### Name Field

"The name field is a string and is required. Users must have a name to sign up."

### Email Field

"For the email field, we'll use fields.Email to validate email addresses."

Phone, Username, and Password Fields

"We'll use fields.String for phone, username, and password. These fields are optional unless specified otherwise."

### Meta Subclass

"Next, we set up the Meta subclass, which is used to specify the fields that might be involved in a payload."

``` python
class Meta: 
        fields = ("id", "name", "email", "phone", "username", "password")
```
### Fields in Meta

"In the Meta subclass, we include all the fields that might be involved in the payload. Although the id field is not required, it might be included when sending data back."

Creating Basic Schemas

#### Single Customer Schema

"For a single customer, we'll instantiate the CustomerSchema."

``` python
customer_schema = CustomerSchema()
```
#### Multiple Customers Schema

"For querying multiple customers (a GET request), we create another schema that can handle a list of customers."

"For security reasons, we'll exclude the password field when querying multiple customers."

```python
customers_schema = CustomerSchema(many=True, exclude=["password"])
```

### Final Setup

"Now that we have our Customer Model and CustomersSchema set up, we're prepared to handle data validation and manage our database."

### Next Steps

"We will now set up our route, controller, and service to handle incoming data and interact with the database."

Database Configuration

"Before we move on, let's make sure everything is hooked up correctly. We’ll create the database tables using the following commands:"

```python
if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    rate_limit_config()

    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.run()
```
"If you need to drop and recreate tables, use db.drop_all() before db.create_all()."

1. **Routing Model Overview**
   - Think of the routing model as separating front-end and back-end processes.
   - Requests are sent to a specific route.
   - The controller processes the request, validating and deserializing data.
   - Data is then handled by the service, which interacts with the model.
   - Finally, the response is sent back to the controller and then to the client.

2. **Process Flow**
   - **Request Handling**: Sent from the browser or Postman to a route.
   - **Controller**: Digests the request, including unpacking the payload, validating data, and deserializing it.
   - **Service**: Receives deserialized data and uses the model to create an object.
   - **Database**: Stores the object and sends a success message back.
   - **Response**: Controller sends a response to the client, such as a success message or the created object.

3. **Building Components**
   - **Route**: Defines the endpoint and method.
   - **Controller**: Manages the data received from the route.
   - **Service**: Handles business logic and data manipulation.
   - **Model**: Represents the data structure.
   ![alt text](image.png)

### Step-by-Step Implementation

1. **Create the Model**
   - Define the data structure and attributes.

2. **Create the Schema**
   - Validate the data against the schema.

3. **Create the Service**
   - Access the database to save customer information.

4. **Define the Controller**
   - Interacts with the service to process data.

5. **Set Up the Route**
   - Define the endpoint and link it to the controller.

### Practical Example

- `create the services folder and create the __init__.py and the customerService.py and enter the following code:`
- `we had an accompanying function. get person get something right? We had that accompanying function. And then this function is really what's going to be broken into 2 parts. Right? So in that function, we received the data from the request. We validated the data as well as deserialize the data.`
- `So that happened in one part. And then we sent that data, or we use that data to create an instance of our database objects, and then we send it along its way.`
- `So that is kind of the 2 prongs. Well, it's really 3, because this will be our route that we'll create on our blueprint. This will be our controller, and then this will be the service that we create.`
![alt text](image-1.png)

`This function will be called by our controller that we set up. So again, that controller is what's going to be manufacturing this data. Probably not be unpacking and deserializing it. And then it's gonna pass it along to this function for us to actually create a new customer from`

1. **Service Creation**
   ```python
   from database import db
   from models.customer import Customer

   def save(customer_data):
       new_customer = Customer(
           name=customer_data['name'],
           email=customer_data['email'],
           password=customer_data['password'],
           phone=customer_data['phone'],
           username=customer_data['username']
       )
       db.session.add(new_customer)
       db.session.commit()
       ## Because we're gonna do a return new customer. there is the potential that during the committing process our customer object or the customer object could be what's called detached from this customer variable. So we want to do a dB dot session. dot refresh(customer)
       db.session.refresh(new_customer)
       return new_customer
    ```
### Controller

- `Create controllers folder`
- `Create __init__.py file in the controllers folder`
- `Create customerController.py file in the controllers folder`
- `this is what's going to actually be receiving and exporting data coming in from requests as well as you know, going out of a request.`

`Handles the incoming request, validates data, and interacts with the service.`

### 1. Customer Controller
- **Purpose**: Handles the reception and sending of data via requests.
- **Key Imports**:
  - `requests` for unpacking incoming requests.
  - `jsonify` to translate data into JSON format before sending it out.

```python
from flask import request, jsonify
from models.schemas.customerSchema import customer_schema
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError


def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201

def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200
```

### 2. Necessary Imports
- **Schema Import**: 
  - Import necessary schemas from models to validate data.
  - Example: `from models.schemas import customer_schema`.

- **Service Import**:
  - Import services without importing individual functions to avoid naming conflicts.
  - Import the whole module: `from services import customer_service`.

### 3. Naming Conventions
- **Consistency**:
  - Always name controller functions the same as the corresponding service functions to maintain consistency.

### 4. Error Handling with Marshmallow
- **Validation**:
  - Use Marshmallow's `validation error` to handle and manage errors related to missing or extra data during validation.
  - Example: `from marshmallow import ValidationError`.

### 5. Try-Except Block
- **Try Block**:
  - Attempt to validate and deserialize incoming data using the schema.
  - Example: 
    ```python
    customer_data = customer_schema.load(request.json)
    ```

- **Except Block**:
  - Catch validation errors and return an error response.
  - Example: 
    ```python
    except ValidationError as e:
        return jsonify(e.messages), 400
    ```

### 6. Saving Customer Data
- **Process**:
  - If validation is successful, pass the data to the service's save function to create and store the customer object in the database.
  - Example:
    ```python
    customer_saved = customer_service.save(customer_data)
    ```

### 7. Returning the Response
- **Response Formation**:
  - Return a JSON response with the saved customer data and a `201` status code for successful creation.
  - Example:
    ```python
    return jsonify(customer_schema.dump(customer_saved)), 201
    ```

### NOW GO BACK TO CUSTOMER BLUEPRINT AND CREATE THIS CUSTOMER ROUTE FOR OURSELVES
- **Blueprint Integration**:
  - Connect the controller logic to the route defined in the blueprint to make the endpoint functional.
  - Example:
    ```python
    from flask import Blueprint
    from controllers.customerController import save, find_all

    customer_blueprint = Blueprint('customer_bp', __name__)

    customer_blueprint.route('/', methods=['POST'])(save)
    customer_blueprint.route('/', methods=['GET'])(find_all)
    ```


# Registering Blueprints in a Flask Application
## Steps
1. Create Route Endpoint
Description: Start by creating a route endpoint that will trigger the controller.
Code Example:
```python
@app.route('/customers', methods=['POST'])
def create_customer():
    # Controller logic here
    pass
```
2. Register the Blueprint in app.py
Description: Now that the route, controller, and model are set up, register the blueprint in the Flask application.
Steps:
Import the blueprint from the routes module:
```python
from routes.customer_bp import customer_blueprint
```
Create a function to register the blueprint:
```python
def blueprints_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
```

Call this function in the application's main runner.
3. Setup URL Prefix
Description: When registering the blueprint, define a URL prefix to group the routes under a common path.
Guidelines:
Use a plural noun for the URL prefix (e.g., /customers).
Code Example:
```python
app.register_blueprint(customer_blueprint, url_prefix='/customers')
```
The whole app.py for reference:
```python
from flask import Flask
from database import db
from models.schemas import ma

from models.customer import Customer

from routes.customerBP import customer_blueprint

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    print('Running')
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.run()
```
4. Test the Setup with Postman
Description: Test the POST route by sending a Raw JSON object to the /customers endpoint using Postman.
Steps:
Create a new collection in Postman.
Set up a POST request to http://localhost:5000/customers.
Create a JSON body for the request:
```json
{
    "name": "Dylan",
    "email": "dylan.k@email.com",
    "phone": "12345678910",
    "username": "DylanK",
    "password": "topsecret"
}
```
Send the request and observe the response.
5. Verify the Correct Response
Description: Upon successfully sending the POST request, verify the response code (e.g., 201 Created) and check that the data is correctly stored.
6. Check MySQL database
`Go to MYSQL Workbench and select the SELECT * FROM customers;`

## `Conclusion`
`And now we pretty much. Whenever we want to add a route or add any features to this customer blueprint, we don't have to go through any more of that setup. we can just create the route, create the controller, and create the service to go along with it, plug all those things in, and we'll have a new route to or for our customers, which is pretty cool.`

- **Initialize Blueprint** (routes folder)
- **Create Model**: database table (models folder)
- **Create Accompanying Schema(s)**: to aid in Validation of data (schemas folder)
- **Do the Following for Each Route**
    - **Create the Service** (services folder): Services serve data to and from the database
    - **Create the Controller** (controllers folder): Controllers validate, serialize, and deserialize, imported and exported data. Send validated data to service to store in database.
    - **Create Route Endpoint** (blueprint file): This route will trigger the controller
- **Register your blueprint** (app.py)

![blueprint](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Vu2ThQPxr72UEOP0LMo4hA.jpeg)

### API Throttling and Rate Limiting:
This is the process of controlling the number of requests that can be made to an API within a certain period, to prevent abuse and ensure the API isn't overwhelmed
https://flask-limiter.readthedocs.io/en/stable/

# `1. install flask-limiter`
```command-line
pip install flask-limiter
pip list
pip freeze
```
# `2. create limiter.py file and add the following code:`
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "3 per second"])#Limter requires key_func to tell it how to target people
#Using get_remote_address tells key_func to target based on IP addresses
```
# `3. Go to app.py add the following, app should look like`
```python
from flask import Flask
from database import db
from models.schemas import ma
from limiter import limiter

from models.customer import Customer

from routes.customerBP import customer_blueprint

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    print('Running')
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')

def rate_limit_config():
    limiter.limit("3 per day")(customer_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    rate_limit_config()

    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.run()
```

# `Test it out on postman`


- **Initialize Limiter** (limiter.py)
- **Configure Limiter on App** (app.py): Set how many times a blueprint can be accessed

```
[count] [per|/] [n (optional)] [second|minute|hour|day|month|year][s]
```

### API Throttling and Rate Limiting

- **Importance:** 
  - Protect APIs and servers from overwhelming traffic.
  - Prevent potential spam attacks or recursive attacks, where someone continuously makes requests to overwhelm the server.
  
- **Implementation:**
  - Set up **rate limiting** to cap the number of requests allowed per second, minute, hour, day, or month.
  - Example: Limit to 200 requests per hour or adjust as needed.

- **Purpose:** 
  - Limit requests to prevent abuse without shutting down the API completely.
  - Use tools to target requests based on specific IP addresses to stop spammers or abusers.
  
- **Steps:**
  - Initialize Flask Limiter and configure it.
  - Import necessary modules (`flask_limiter` and `get_remote_address`).
  - Set up the limiter to track and limit requests based on IP addresses.
  
- **Code Example:**
  ```python
  from flask_limiter import Limiter
  from flask_limiter.util import get_remote_address

  limiter = Limiter(key_func=get_remote_address)

  # Initialize in the app
  limiter.init_app(app)

  # Set up a limit
  @limiter.limit("5 per day")
  def my_route():
      return "This route is limited to 5 requests per day"
    ```
#### Configuration Options:

Set default limits, such as a maximum of 200 requests per day, 50 per hour, etc.
Consider additional configurations to fine-tune the API protection based on different request rates.
Installation Command:

```bash
pip install Flask-Limiter
```
#### Final Thoughts:
Rate limiting is crucial for protecting APIs from misuse.
Configurations should be adjusted based on the expected use case and potential threats.

### Caching:
Caching is the process of storing frequently access data in memory, to reduce the number of queries that need to be made. This not only reduce traffic to your database but also increases the speed of retrieval.

The downside to caching is that it is not updated as frequently, so while you get the info faster there is a chance it is incomplete.
```
pip install flask-caching
```
- **Instantiate Cache** (cache.py)
- **Add Cache Type to Config** (config.py)
- **Initialize Cache on App** (app.py)
- **Wrap the Controllers you wish to Cache** (controllers folder)


# Caching
Introduction to Caching
Start the lesson with the concept of caching:

"Caching is a powerful concept in optimizing the performance of web applications. It allows us to store frequently accessed data in a temporary storage location, making future access to this data much faster. Let's dive into how caching works."

## Explanation of Caching
**Define caching:**

"Caching is essentially a small memory deposit that we create for specific routes. We only create caches for routes that are heavily accessed. This ensures that the data can be retrieved quickly without the need to repeatedly query the database."

Provide an example:

"For instance, imagine an ecommerce website where the homepage displays the top 20 products. The homepage is frequently visited, so caching the data for these top products can save time. Instead of querying the database every time a user visits the homepage, we can use the cached version."

How Caching Works
Illustrate the caching process:

"Think of caching as a middle man between the frontend user and the database. We store the frequently accessed data in the cache so that whenever a user requests this data, we serve it from the cache instead of going all the way to the database."

"This reduces the number of queries made to the database and increases the speed of data retrieval, as accessing data from memory is much faster than querying a database."

Draw a simple diagram:

```css
[Frontend User] --> [Cache] --> [Database]
```
"If the data is available in the cache, the request is served from there. If not, it goes to the database, and the cache is updated with the new data."

### Benefits and Downsides of Caching
Discuss the benefits:

"The primary benefit of caching is the reduction in the number of database queries, which in turn reduces traffic to the database and increases the speed of data retrieval."

Address the downsides:

"However, caching does occupy local memory, so it’s important to only cache frequently accessed material. Additionally, caches aren’t updated very frequently. Typically, they refresh every 60 seconds to stay up-to-date with any changes in the database."

"This means there's a trade-off between speed and freshness of data. For most use cases, a slight delay in data freshness is acceptable for the performance gain."

Implementing Caching in Code
Introduce the practical part:

"Let's implement caching in our application. We'll use Flask-Caching for this purpose. First, we'll install the necessary package."

Install Flask-Caching:

```bash
pip install Flask-Caching
pip freeze > requirements.txt
```
Set up caching in a new file caching.py:

```python
from flask_caching import Cache

cache = Cache()
```
Add cache configuration in config.py:

```python
CACHE_TYPE = 'simple'
"We're using a simple cache type for simplicity's sake."
```
Initialize the cache in your app:

```python
from caching import cache

cache.init_app(app)
```
"We’re now ready to use the cache in our app."

Wrap a route with the cache decorator:

"Let's wrap a specific route in the cache. For example, we'll cache the route that retrieves all customers from our database."

```python
from flask import Flask
from caching import cache

app = Flask(__name__)

@app.route('/customers')
@cache.cached(timeout=60)
def get_customers():
    # Your database query logic here
    return customers_list
```
"Here, we’ve set a timeout of 60 seconds. This means that the cache will refresh every 60 seconds."

### `so really quickly, I'm going to go ahead and add in a an additional route. So we're gonna have a an actual querying route to get all of our customers out of our database. So we're going to come over here to our services and start again from the bottom up.`

### `Inside customerServices.py add:`
```python
def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers
```

### `Go to customerController.py and add:`
```python
from models.schemas.customerSchema import customer_schema, customers_schema
from caching import cache

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200
```

### `Go to the customerBP.py and add the following...`
```python
from controllers.customerController import save, find_all

customer_blueprint.route('/', methods=['GET'])(find_all)
```

### `In Postman make a GET request to /customers`

### `Show that it takes 13ms and then do the caching`

### `Go to customerController.py and wrap a controller with caching

```python
from caching import cache

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200
```