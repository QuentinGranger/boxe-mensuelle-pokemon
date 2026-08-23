"""Generate Apple Calendar ICS from Pokemon boxes with product links."""

from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
OUTPUT = BASE / "output"


def create_calendar_event(box):
    products = ""
    for product in box.get("products", []):
        products += f" {product.get('name', '')}: {product.get('url', '')}"

    description = f"{box.get('description', '')} Budget: {box.get('budget', 0)} EUR. Produits:{products}"

    return f"""BEGIN:VEVENT
UID:{box['id']}
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{box['date']}T090000
SUMMARY:{box['title']}
DESCRIPTION:{description}
END:VEVENT
"""


def generate_calendar(boxes):
    content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Pokemon Monthly Box//FR//",
        "X-WR-CALNAME:Pokemon Monthly Box",
        "X-WR-CALDESC:Calendrier des box Pokemon mensuelles"
    ]

    for box in boxes:
        content.append(create_calendar_event(box))

    content.append("END:VCALENDAR")

    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "pokemon-monthly-box.ics").write_text("\r\n".join(content), encoding="utf-8")


if __name__ == "__main__":
    generate_calendar([])
