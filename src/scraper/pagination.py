from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from .get_soup import get_soup
import re


def get_next_page(base_url):
    soup = get_soup(base_url)
    if not soup:
        return []

    page_urls = set()
    page_urls.add(base_url)

    pagination_links = soup.select("a.andes-pagination__link")

    max_page = 1

    for link in pagination_links:
        href = link.get("href")
        if href and "page=" in href:
            match = re.search(r"page=(\d+)", href)
            if match:
                num = int(match.group(1))
                if num > max_page:
                    max_page = num

    print(f"Max page found: {max_page}")

    pages = []
    parsed_url = urlparse(base_url)
