import json
import os
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent


def load_restaurant() -> dict:
    with open(ROOT / "restaurant.json") as f:
        return json.load(f)


def load_faq() -> list[dict]:
    with open(ROOT / "faq.json") as f:
        return json.load(f)


def today() -> date:
    """The restaurant's local date. ASSISTANT_TODAY (YYYY-MM-DD) pins it for tests and replays."""
    pinned = os.environ.get("ASSISTANT_TODAY")
    if pinned:
        return date.fromisoformat(pinned)
    return datetime.now(ZoneInfo(load_restaurant()["timezone"])).date()
