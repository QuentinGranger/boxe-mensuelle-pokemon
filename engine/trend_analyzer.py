"""Pokemon Concierge trend analysis module.

Designed to collect and score monthly themes before generating the calendar.
"""

from datetime import datetime


def analyze_month():
    month = datetime.now().strftime('%B %Y')

    return {
        "period": month,
        "focus": "Découverte et collection Pokémon",
        "signals": [
            "Sorties officielles à surveiller",
            "Pokémon populaires de la communauté",
            "Opportunités de collection",
        ],
        "recommendation": "Analyser avant achat et privilégier les objets avec une histoire.",
    }


def score_theme(theme):
    return {
        "emotion": theme.get("emotion", 0),
        "collection": theme.get("collection", 0),
        "value": theme.get("value", 0),
    }
