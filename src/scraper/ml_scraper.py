from .get_soup import get_soup
from .extract_product import extract_product_data
from .pagination import get_next_page


def get_all_products(base_url):
    products = []

    urls = get_next_page(base_url)

    for url in urls:
        print(f"Scraping URL: {url}")
        soup = get_soup(url)

        if not soup:
            continue

        products_blocks = soup.select(
            ".andes-card.poly-card.poly-card--grid-card.poly-card--large.andes-card--flat.andes-card--padding-0.andes-card--animated")

        for block in products_blocks:
            data = extract_product_data(block)
            if data:
                products.append(data)

    return products
