"""Generate Apple Calendar ICS from Pokemon boxes."""

from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
OUTPUT = BASE / "output"


def create_calendar_event(title, description, date):
    return f"""BEGIN:VEVENT
UID:{date}-{title.replace(' ', '-')}
DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{date}T090000
SUMMARY:{title}
DESCRIPTION:{description}
END:VEVENT
"""


def generate_calendar(boxes):
    content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Pokemon Monthly Box//FR//"
    ]

    for box in boxes:
        content.append(
            create_calendar_event(
                box["title"],
                box["description"],
                box["date"]
            )
        )

    content.append("END:VCALENDAR")

    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "pokemon-monthly-box.ics").write_text("\n".join(content))


if __name__ == "__main__":
    generate_calendar([])
