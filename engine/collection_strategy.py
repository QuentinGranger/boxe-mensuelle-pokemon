"""Conseils de conservation et stratégie collection."""


def classify_collection_item(item):
    score = item.get("score", 0)
    if score >= 80:
        return "conserver"
    if score >= 60:
        return "exposer"
    return "utiliser_ou_ouvrir"


def build_strategy(items):
    return [
        {
            "item": item.get("name"),
            "action": classify_collection_item(item)
        }
        for item in items
    ]
