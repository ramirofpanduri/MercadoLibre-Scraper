from datetime import datetime, timezone
import re
from .utils import extract_product_image_id


def extract_product_data(product):
    try:
        title = product.select_one(".poly-component__title-wrapper")
        seller = product.select_one(".poly-component__seller")
        price = product.select_one(".andes-money-amount__fraction")
        image_tag = product.select_one(".poly-component__picture")

        image_url = image_tag.get("data-src") or image_tag.get("src")
        image_id = extract_product_image_id(image_url) if image_url else None
        return {
            "title": title.get_text(strip=True) if title else None,
            "image_id": image_id,
            "seller": seller.get_text(strip=True) if seller else None,
            "price": price.get_text(strip=True) if price else None,
            "image": image_url,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    except Exception as e:
        print(f"Error extracting product data: {e}")
        return None
