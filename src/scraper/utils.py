import re


def extract_product_image_id(image_url):
    match = re.search(r"(MLA\d+)", image_url)
    return match.group(1) if match else None
