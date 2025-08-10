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

        for p in unique_products:
            prod = Product(
                product_id=p['product_id'],
                title=p['title'],
                seller=p['seller'],
                price=p['price'],
                image=p['image'],
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )
            session.merge(prod)

        scraped_ids = {p['product_id'] for p in unique_products}
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
