from marshmallow import fields
from . import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchema', many=True)
    customer = fields.Nested("CustomerOrderSchema")

    class Meta:
        fields = ('id', 'date', 'customer_id', 'product_ids', 'products', 'customer')

# Create an instance of the OrderSchema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)  # For handling multiple orders



    ## In MySQL, we would see the table Customers with the columns id, name, email, phone, username, and password. We wouldn't see the orders column because it's a relationship, not a column.

    ## Any Customer object that we query from the database will have an orders attribute that contains a list of Order objects associated with that Customer object.

    ## I can look at the orders attribute of a Customer object and that will point me to the Order objects associated with that Customer object.

    ## I don't to do any joins or queries to get the Order objects associated with a Customer object. I can just look at the orders attribute of the Customer object.

    ## This is the power of SQLAlchemy and the ORM. It allows me to easily navigate relationships between tables in a database.

    ## Our Schemas are set up to only show the table columns and not the relationships. We need to add the relationships to the schemas so that we can see the relationships in the JSON response.
    
    ## We will set it up to see all of the products that are associated with an order. We will do this by creating a schema for the Product object and using the ma.Nested() field in the Order schema.
    

    ### Gp tp Postman and make a get request to http://localhost:5000/orders and we should see the orders that are in the database

    ## We can do a lot with that, we can figure out whos the customer associated with the order, we can figure out what products are associated with the order, we can figure out the date of the order, etc.

    ## We can do this through MYSQL queries, but we can also do this through the ORM which is way better. We can do this by looking at the attributes of the Order object that we query from the database.

    ## all we have to do is setup our schema to show what's housed in this products attribute. We can do this by creating a schema for the Product object and using the ma.Nested() field in the Order schema.

    ## GO UP TO THE CODE AND ADD THE PRODUCTS ATTRIBUTE TO THE ORDER SCHEMA
    ## Products is going to connect me to the Products attribute.
    ## Well what does a product look like? Well, a product looks like our ProductSchema we already have! So we can just use that schema to show what a product looks like.
    ## So now whenever we are using the OrderSchema, there are going to be products associated with it. We can see what those products look like by looking at the ProductSchema.
    ## Serialize the products so that they can be seen in my JSON response.

    ## Now when we query this data, we can see all the information associated with the order. This is great because if we are thinking from a frontend perspective, we can see all the information associated with the order. We can see the customer, the products, the date, etc. for the user to see.

    ## If we want to see our Customers information, we can do the same thing. We can create a schema for the Customer object and use the ma.Nested() field in the Order schema to show the customer information in the JSON response.
        ## So go to the Customers schema and add the orders attribute to the Customer schema and then go to the Order schema and add the customer attribute to the Order schema. This will allow us to see the customer information in the JSON response.