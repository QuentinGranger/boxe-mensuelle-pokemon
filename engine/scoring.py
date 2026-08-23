"""Calcul du score collector."""

WEIGHTS = {
    "popularity": 0.30,
    "collector": 0.25,
    "rarity": 0.20,
    "price_value": 0.15,
    "nostalgia": 0.10
}


def score_product(product):
    return (
        product.get("popularity", 0) * WEIGHTS["popularity"] +
        product.get("collector_score", 0) * WEIGHTS["collector"] +
        product.get("rarity", 0) * WEIGHTS["rarity"] +
        product.get("price_value", 0) * WEIGHTS["price_value"] +
        product.get("nostalgia", 0) * WEIGHTS["nostalgia"]
    )
