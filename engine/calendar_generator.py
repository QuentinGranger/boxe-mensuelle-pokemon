"""
Pokémon Concierge - Dynamic iCal generator

Generates docs/pokemon-concierge.ics for Apple Calendar subscriptions.
The file is regenerated automatically by GitHub Actions.
"""

from datetime import datetime, timezone
from pathlib import Path
import json
import calendar

BASE = Path(__file__).parent.parent
OUTPUT = BASE / "docs" / "pokemon-concierge.ics"
HISTORY = BASE / "history"


def build_monthly_adventure():
    now = datetime.now()
    month = now.month

    seasonal_themes = {
        10: {
            "theme": "🎃 Halloween Pokémon",
            "pokemon": "Ectoplasma, Mimiqui et les Pokémon Spectre",
            "story": "Une expédition nocturne à la recherche des mystères Pokémon.",
        },
        12: {
            "theme": "🎄 Noël Pokémon",
            "pokemon": "Pikachu, Évoli et les Pokémon de glace",
            "story": "Une aventure hivernale placée sous le signe du partage.",
        },
        2: {
            "theme": "❤️ Pokémon partenaires",
            "pokemon": "Évoli et les Pokémon attachants",
            "story": "Une célébration du lien entre le dresseur et son équipe.",
        },
        7: {
            "theme": "☀️ Grande aventure Pokémon",
            "pokemon": "Pokémon explorateurs",
            "story": "Un voyage Pokémon inspiré des grandes explorations.",
        },
    }

    data = seasonal_themes.get(month, {
        "theme": "🌟 Nouvelle aventure Pokémon",
        "pokemon": "Pokémon du mois",
        "story": "Un nouveau chapitre dans le voyage du dresseur.",
    })

    data.update({
        "year": now.year,
        "month": month,
        "month_name": calendar.month_name[month],
        "score": 85,
        "verdict": "🟢 Badge obtenu : recommandé",
        "budget": "50 € maximum",
    })

    return data


def write_history(data):
    HISTORY.mkdir(exist_ok=True)
    path = HISTORY / f"{data['year']}-{data['month']:02d}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def generate_ics(data):
    description = (
        f"Pokémon Concierge Légendaire\\n\\n"
        f"Expédition : {data['theme']}\\n"
        f"Pokémon vedettes : {data['pokemon']}\\n\\n"
        f"{data['story']}\\n\\n"
        f"Budget : {data['budget']}\\n"
        f"Score : {data['score']}/100\\n"
        f"Verdict : {data['verdict']}"
    )

    content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Pokemon Concierge//Dynamic Calendar//FR
CALSCALE:GREGORIAN
X-WR-CALNAME:Pokemon Concierge Legendaire
BEGIN:VEVENT
UID:pokemon-concierge-{data['year']}-{data['month']:02d}@github.com
DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{data['year']}{data['month']:02d}01T100000
DTEND:{data['year']}{data['month']:02d}01T103000
SUMMARY:{data['theme']} - Pokémon Monthly Experience
DESCRIPTION:{description}
RRULE:FREQ=MONTHLY;BYMONTHDAY=1
END:VEVENT
END:VCALENDAR
"""

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    adventure = build_monthly_adventure()
    write_history(adventure)
    generate_ics(adventure)
    print("Pokémon Concierge calendar generated")
