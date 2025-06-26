from .scraper.ml_scraper import get_all_products


def main():
    url = "https://www.mercadolibre.com.ar/ofertas?domain_id=MLA-CELLPHONES&container_id=MLA779505-1#deal_print_id=4ae460f0-52b3-11f0-ac2b-8f126b64e4a0&c_tracking_id=4ae460f0-52b3-11f0-ac2b-8f126b64e4a0"
    products = get_all_products(url)

    print(f"Products found: {len(products)}\n")

    for i, product in enumerate(products, start=1):
        print(f"Product {i}:")
        for k, v in product.items():
            print(f"   {k}: {v}")
        print("-" * 40)


if __name__ == "__main__":
    main()
