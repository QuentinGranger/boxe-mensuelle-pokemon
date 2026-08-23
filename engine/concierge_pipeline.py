"""Pipeline central du Pokémon Concierge.

Assemble les briques : tendances, produits, scoring et expérience.
"""

from datetime import datetime
from engine.trend_analyzer import analyze_month
from engine.experience_builder import build_experience
from engine.product_ranker import rank_products


def generate_monthly_experience(products=None):
    month = datetime.now().strftime('%B %Y')
    trends = analyze_month()
    ranked = rank_products(products or [])
    experience = build_experience(trends, ranked)

    return {
        "month": month,
        "trends": trends,
        "experience": experience,
        "products": ranked,
    }
