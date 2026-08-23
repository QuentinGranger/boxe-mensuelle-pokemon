"""Find the best product combination under a budget."""


def optimize_budget(products, budget):
    selected = []
    total = 0

    ranked = sorted(products, key=lambda x: x.get("score", x.get("collector_score", 0)), reverse=True)

    for item in ranked:
        price = item.get("price", item.get("estimated_price", 0))
        if total + price <= budget:
            selected.append(item)
            total += price

    return {
        "budget": budget,
        "items": selected,
        "total": total,
        "remaining": budget - total,
        "collection_score": round(sum(i.get("collector_score", 0) for i in selected), 2)
    }
