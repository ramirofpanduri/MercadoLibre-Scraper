import re


def extract_product_image_id(image_url):
    match = re.match(r"MLA\d+", image_url)
    return match.group(0) if match else None
