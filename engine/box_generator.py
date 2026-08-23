"""Generate a Pokemon monthly box from products and themes."""
import json
from pathlib import Path
from .scoring import score_product
from .budget_optimizer import optimize_budget

BASE = Path(__file__).parent.parent


def load_products():
    products = []
    for file in (BASE / "products").glob("*.json"):
        try:
            data = json.loads(file.read_text())
            products.extend(data if isinstance(data, list) else data.get("products", []))
        except Exception:
            continue
    return products


def generate_box(theme, budget=50):
    products = load_products()
    matches = [p for p in products if theme in p.get("themes", [])]
    matches.sort(key=score_product, reverse=True)
    return optimize_budget(matches, budget)


if __name__ == "__main__":
    print(generate_box("spectres", 50))
