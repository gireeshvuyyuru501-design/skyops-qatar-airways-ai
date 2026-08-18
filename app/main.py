from fastapi import FastAPI
from app.config import get_settings
from app.models import (
    AssistRequest,
    AssistResponse,
    DisruptionRequest,
    FlightSearchRequest,
)
from app.services.repository import search_flights
from app.services.workflows import assist, handle_disruption


settings = get_settings()
app = FastAPI(
    title="SkyOps AI — Qatar Airways Inspired Airline Operations Assistant",
    version="1.0.0",
    description=(
        "Unofficial portfolio demo using simulated airline data. "
        "Not affiliated with or endorsed by Qatar Airways."
    ),
)


@app.get("/")
def root() -> dict:
    return {
        "project": "SkyOps AI",
        "type": "Qatar Airways inspired airline-operations portfolio demo",
        "official": False,
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict:
    return {
        "status": "healthy",
        "openai_enabled": bool(settings.openai_api_key),
        "model": settings.openai_model,
    }


@app.post("/flights/search")
def flights_search(request: FlightSearchRequest) -> dict:
    flights = search_flights(request.origin, request.destination)
    return {
        "origin": request.origin.upper(),
        "destination": request.destination.upper(),
        "count": len(flights),
        "flights": flights,
    }


@app.post("/assist", response_model=AssistResponse)
def passenger_assist(request: AssistRequest) -> AssistResponse:
    return AssistResponse(**assist(request.question))


@app.post("/disruption")
def disruption(request: DisruptionRequest) -> dict:
    return handle_disruption(request.flight_number, request.issue)


@app.post("/evaluate")
def evaluate() -> dict:
    checks = {
        "health": True,
        "flight_search": len(search_flights("DOH", "JFK")) >= 1,
        "policy_retrieval": bool(assist("What is the baggage policy?")["sources"]),
        "disruption_found": handle_disruption("QR739", "delay")["flight_found"],
        "human_confirmation": any(
            "human" in item.lower()
            for item in handle_disruption("QR739", "delay")["recommendations"]
        ),
    }
    passed = sum(checks.values())
    return {
        "total": len(checks),
        "passed": passed,
        "failed": len(checks) - passed,
        "checks": checks,
    }
