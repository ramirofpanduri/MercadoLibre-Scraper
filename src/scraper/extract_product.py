from datetime import datetime, timezone
import re


def extract_product_data(product):
    try:
        title = product.select_one(".poly-component__title-wrapper")
        seller = product.select_one(".poly-component__seller")
        price = product.select_one(".andes-money-amount__fraction")
        image_tag = product.select_one("img")

        if image_tag:
            image_url = image_tag.get("data-src") or image_tag.get("src")
        else:
            image_url = None

        link_tag = product.select_one("a")
        product_url = link_tag.get("href") if link_tag else None

        product_id = None
        if product_url:
            match = re.search(r"(MLA\d+)", product_url)
            if match:
                product_id = match.group(1)

        if not product_id:
            return None
        if not image_url or image_url.startswith("data:image/gif;base64"):
            image_url = None

        return {
            "title": title.get_text(strip=True) if title else None,
            "product_id": product_id,
            "seller": seller.get_text(strip=True) if seller else None,
            "price": price.get_text(strip=True) if price else None,
            "image": image_url,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    except Exception as e:
        print(f"Error extracting product data: {e}")
        return None
