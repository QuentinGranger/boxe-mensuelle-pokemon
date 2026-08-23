"""Builds the narrative layer of a Pokemon monthly experience."""


def build_expedition(theme):
    return {
        "name": theme.get("name", "Expédition Pokémon du mois"),
        "pokemon": theme.get("pokemon", "Pokémon mystère"),
        "region": theme.get("region", "À découvrir"),
        "story": theme.get("story", "Un nouveau chapitre de l'aventure Pokémon."),
        "ritual": [
            "Découvrir la sélection",
            "Installer ou utiliser les objets",
            "Ajouter un souvenir à la collection",
        ],
    }
