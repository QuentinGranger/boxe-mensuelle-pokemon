def optimize_budget(products, budget):
    selected = []
    total = 0

    ranked = sorted(products, key=lambda x: x.get('score', 0), reverse=True)

    for item in ranked:
        price = item.get('price', 0)
        if total + price <= budget:
            selected.append(item)
            total += price

    return {
        'items': selected,
        'total': total,
        'remaining': budget - total
    }
