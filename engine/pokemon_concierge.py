from datetime import datetime
from pathlib import Path

OUTPUT = Path("output/pokemon-concierge.ics")


def create_event():
    year = datetime.now().year
    month = datetime.now().month

    title = "🎁 Pokémon Monthly Experience - Concierge Légendaire"

    description = """Pokémon Concierge Légendaire

Rituel mensuel du dresseur :

🌐 Pokédex du mois
- Actualités Pokémon
- Sorties officielles
- Jeux vidéo, anime, TCG et produits dérivés
- Tendances et opportunités

🗺️ Expédition Pokémon
- Nouveau thème mensuel
- Pokémon mascotte
- Région, génération et histoire

📦 Box personnalisée (50€ maximum)
- TCG
- Peluches
- Figurines
- Livres
- Jeux
- Objets collector

🏛️ Conseil de conservateur
- À garder
- À exposer
- À utiliser
- À ouvrir

⭐ Verdict
Acheter / Attendre / Économiser

Objectif : construire une collection Pokémon avec une histoire personnelle.
"""

    ics = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Pokemon Concierge Legendaire//FR
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:pokemon-concierge-{year}-{month}@github.com
DTSTART:20260901T100000
RRULE:FREQ=MONTHLY;BYMONTHDAY=1
SUMMARY:{title}
DESCRIPTION:{description.replace(chr(10), '\\n')}
END:VEVENT
END:VCALENDAR
"""

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(ics, encoding="utf-8")


if __name__ == "__main__":
    create_event()
