from datetime import datetime

from pokemon_center import fetch_products as pokemon_center
from fnac import fetch_products as fnac
from micromania import fetch_products as micromania
from cultura import fetch_products as cultura
from boutiques_tcg import fetch_products as boutiques_tcg


SCRAPERS = [
    pokemon_center,
    fnac,
    micromania,
    cultura,
    boutiques_tcg
]


def update_database():
    products = []

    for scraper in SCRAPERS:
        try:
            products.extend(scraper())
        except Exception:
            continue

    return {
        "updated_at": datetime.now().isoformat(),
        "products": products
    }


if __name__ == '__main__':
    print(update_database())
