from datetime import datetime


def extract_product_data(product):
    try:
        title = product.select_one(".poly_component_title")
        seller = product.select_one(".poly_component_seller")
        price = product.select_one(".poly-price__current")
        image_tag = product.select_one(".poly-card__portada img")

        return {
            "title": title.get_text(strip=True) if title else None,
            "seller": seller.get_text(strip=True) if seller else None,
            "price": price.get_text(strip=True) if price else None,
            "image": image_tag["src"] if image_tag else None,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        print(f"Error extracting product data: {e}")
        return None
