from scraper.get_soup import get_soup


def main():
    url = "https://www.mercadolibre.com.ar/ofertas?domain_id=MLA-CELLPHONES&container_id=MLA779505-1#deal_print_id=d4772d90-5063-11f0-a3cb-83c2abbbf356&c_tracking_id=d4772d90-5063-11f0-a3cb-83c2abbbf356"
    soup = get_soup(url)

    if soup:
        print(soup.title.string)


if __name__ == "__main__":
    main()
