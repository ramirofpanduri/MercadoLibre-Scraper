import datetime
from .models import Product
from .db import SessionLocal
from sqlalchemy import select
import traceback


def save_products(scraped_products):
    session = SessionLocal()
    try:

        seen = set()
        unique_products = []
        for p in scraped_products:
            pid = str(p['product_id']).strip().upper()
            if pid not in seen:
                seen.add(pid)
                p['product_id'] = pid
                unique_products.append(p)

        scraped_ids = {p['product_id'] for p in scraped_products}

        existing_products = session.execute(
            select(Product).where(Product.product_id.in_(scraped_ids))
        ).scalars().all()
        existing_dict = {prod.product_id: prod for prod in existing_products}

        for p in scraped_products:
            prod = existing_dict.get(p['product_id'])
            if prod:
                prod.title = p['title']
                prod.seller = p['seller']
                prod.price = p['price']
                prod.image = p['image']
                prod.timestamp = datetime.datetime.now(datetime.timezone.utc)
            else:
                new_product = Product(
                    product_id=p['product_id'],
                    title=p['title'],
                    seller=p['seller'],
                    price=p['price'],
                    image=p['image'],
                    timestamp=datetime.datetime.now(datetime.timezone.utc)
                )
                session.add(new_product)

        all_products = session.execute(select(Product)).scalars().all()
        for product in all_products:
            if product.product_id not in scraped_ids:
                session.delete(product)

        session.commit()

    except Exception as e:
        session.rollback()
        traceback.print_exc()
        print(f"Error saving products: {e}")
    finally:
        session.close()
