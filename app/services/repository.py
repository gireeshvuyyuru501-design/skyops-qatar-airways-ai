import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / "data"


def load_flights() -> list[dict]:
    return json.loads((BASE / "flights.json").read_text(encoding="utf-8"))


def load_policies() -> list[dict]:
    return json.loads((BASE / "policies.json").read_text(encoding="utf-8"))


def search_flights(origin: str, destination: str) -> list[dict]:
    origin = origin.upper()
    destination = destination.upper()
    return [
        f for f in load_flights()
        if f["origin"] == origin and f["destination"] == destination
    ]


def find_flight(flight_number: str) -> dict | None:
    needle = flight_number.upper()
    return next((f for f in load_flights() if f["flight_number"] == needle), None)


def retrieve_policies(query: str, top_k: int = 2) -> list[dict]:
    query_terms = set(query.lower().split())
    scored = []
    for item in load_policies():
        haystack = f'{item["title"]} {item["content"]}'.lower()
        score = sum(1 for term in query_terms if term in haystack)
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    results = [item for score, item in scored if score > 0][:top_k]
    return results or load_policies()[:1]
