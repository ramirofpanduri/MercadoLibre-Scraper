from models import Product
from db import SessionLocal


def save_products(products):
    session = SessionLocal()
    try:
        for p in products:
            product = Product(
                title=p['title'],
                seller=p['seller'],
                price=p['price'],
                image=p['image'],
                timestamp=p['timestamp'],
            )
            session.add(product)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error saving products: {e}")
    finally:
        session.close()
