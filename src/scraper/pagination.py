from .get_soup import get_soup
from urllib.parse import urljoin


def get_next_page(base_url):
    soup = get_soup(base_url)
    if not soup:
        return []

    page_urls = [base_url]

    pagination_links = soup.select("a.andes.pagination__link")

    for link in pagination_links:
        href = link.get("href")
        if href:
            full_url = urljoin(base_url, href)
            if full_url not in page_urls:
                page_urls.append(full_url)

    return page_urls
