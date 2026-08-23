"""Cardmarket scraper adapter.
Returns normalized Pokemon products.
"""


def fetch_products():
    return []


def normalize_product(name, price, url):
    return {
        "name": name,
        "price": price,
        "url": url,
        "source": "Cardmarket",
        "stock": True
    }
