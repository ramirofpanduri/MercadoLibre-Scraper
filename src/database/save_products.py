import datetime
from models import Product
from db import SessionLocal
from sqlalchemy import select


def save_products(scraped_products):
    session = SessionLocal()
    try:
        scraped_ids = set()
        for p in scraped_products:
            scraped_ids.add(p['product_id'])
            existing_product = session.execute(
                select(Product).where(Product.product_id == p['product_id'])
            ).scalar_one_or_none()

            if existing_product:
                existing_product.title = p['title']
                existing_product.seller = p['seller']
                existing_product.price = p['price']
                existing_product.image = p['image']
                existing_product.timestamp = datetime.datetime.now(
                    datetime.timezone.utc)
            else:
                product = Product(
                    product_id=p['product_id'],
                    title=p['title'],
                    seller=p['seller'],
                    price=p['price'],
                    image=p['image']
                )
                session.add(product)

        existing_product = session.execute(select(Product)).scalars().all()
        for product in existing_product:
            if product.product_id not in scraped_ids:
                session.delete(product)

        session.commit()

    except Exception as e:
        session.rollback()
        print(f"Error saving products: {e}")
    finally:
        session.close()
