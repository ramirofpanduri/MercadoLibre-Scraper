from urllib.parse import urljoin
from .get_soup import get_soup
import re


def get_next_page(base_url):
    soup = get_soup(base_url)
    if not soup:
        return []

    page_urls = set()
    page_urls.add(base_url)

    pagination_links = soup.select("a.andes-pagination__button")

    for link in soup.select("a.andes-pagination__link"):
        href = link.get("href")
        if href and "page=" in href:
            full_url = urljoin(base_url, href)
            page_urls.add(full_url)

    def sort_key(url):
        match = re.search(r"page=(\d+)", url)
        return int(match.group(1)) if match else 0

    sorted_urls = sorted(page_urls, key=sort_key)

    print("[🔗] Páginas encontradas:")
    for l in pagination_links:
        print("   ", l)
    return sorted_urls
