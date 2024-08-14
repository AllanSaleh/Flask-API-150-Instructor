from models.product import Product
from database import db
from sqlalchemy import select


def save(product_data):
    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)    
    return new_product

def find_all():
    query = select(Product)
    all_productss = db.session.execute(query).scalars().all()
    return all_productss

## % is a wildcard character that represents zero or more characters
## .scalar() returns the first column of the first row of the result set
## where does the search_product return to? Answer: It returns to the controller
def search_product(search_term):
    query = select(Product).where(Product.name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products