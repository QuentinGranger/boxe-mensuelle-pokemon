"""Ranks Pokemon products for the Concierge experience."""


def rank_product(product):
    score = 0

    score += product.get("emotion", 0)
    score += product.get("collection", 0)
    score += product.get("quality", 0)

    if product.get("official", False):
        score += 10

    return score


def classify(score):
    if score >= 80:
        return "Badge obtenu : recommandé"
    if score >= 50:
        return "En observation : attendre"
    return "Rencontre à éviter"
