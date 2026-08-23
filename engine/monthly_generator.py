"""Dynamic Pokemon monthly box generator."""

from pathlib import Path
import json
from datetime import datetime

from box_generator import generate_box

BASE = Path(__file__).parent.parent
OUTPUT = BASE / "output"


def generate_monthly_box(month, year, theme, budget=50):
    box = generate_box(theme, budget)

    result = {
        "month": month,
        "year": year,
        "title": f"Pokemon Monthly Box - {month} {year}",
        "theme": theme,
        "description": f"Box Pokemon mensuelle autour du theme {theme}",
        "budget": budget,
        "products": box.get("items", []),
        "total": box.get("total", 0),
        "collection_score": 0,
        "investment_score": 0,
        "generated_at": datetime.now().isoformat()
    }

    OUTPUT.mkdir(exist_ok=True)
    filename = OUTPUT / f"{month.lower()}-{year}.json"
    filename.write_text(json.dumps(result, indent=2, ensure_ascii=False))

    return result


if __name__ == "__main__":
    print(generate_monthly_box("January", 2027, "hiver", 50))
