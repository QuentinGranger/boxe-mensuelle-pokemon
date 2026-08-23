import json
from pathlib import Path

BASE = Path(__file__).parent.parent


def load_products():
    products = []
    for file in (BASE / 'products').glob('*.json'):
        data = json.loads(file.read_text())
        products.extend(data.get('products', []))
    return products


def generate_box(theme, budget=50):
    products = load_products()
    matches = [p for p in products if theme in p.get('themes', [])]
    matches.sort(key=lambda x: x.get('collector_score', 0), reverse=True)

    result = []
    total = 0
    for product in matches:
        if total + product['price'] <= budget:
            result.append(product)
            total += product['price']

    return {
        'theme': theme,
        'budget': budget,
        'total': total,
        'items': result
    }


if __name__ == '__main__':
    print(generate_box('collection'))
