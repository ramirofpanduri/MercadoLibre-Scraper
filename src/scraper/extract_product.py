from datetime import datetime, timezone


def extract_product_data(product):
    try:
        title = product.select_one(".poly-component__title-wrapper")
        seller = product.select_one(".poly-component__seller")
        price = product.select_one(".andes-money-amount__fraction")
        image_tag = product.select_one(".poly-component__picture")

        return {
            "title": title.get_text(strip=True) if title else None,
            "seller": seller.get_text(strip=True) if seller else None,
            "price": price.get_text(strip=True) if price else None,
            "image": image_tag["data-src"] if image_tag else None,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    except Exception as e:
        print(f"Error extracting product data: {e}")
        return None
