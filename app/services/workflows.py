from app.services.repository import (
    find_flight,
    retrieve_policies,
    search_flights,
)
from app.services.ai_service import generate_answer


def assist(question: str) -> dict:
    policies = retrieve_policies(question)
    context = "\n".join(
        f'{p["title"]}: {p["content"]}'
        for p in policies
    )
    answer, model = generate_answer(question, context)
    return {
        "answer": answer,
        "sources": [p["title"] for p in policies],
        "action_recommendations": [
            "Verify itinerary and ticket details",
            "Escalate booking changes to a human agent",
        ],
        "model_used": model,
    }


def handle_disruption(flight_number: str, issue: str) -> dict:
    flight = find_flight(flight_number)
    if not flight:
        return {
            "flight_found": False,
            "flight_number": flight_number.upper(),
            "issue": issue,
            "recommendations": ["Verify the flight number with a human agent."],
        }

    alternatives = search_flights(flight["origin"], flight["destination"])
    recommendations = [
        "Confirm the latest operational status",
        "Check connection impact and passenger priority",
        "Offer alternative itinerary options where available",
        "Require human confirmation before rebooking",
    ]
    return {
        "flight_found": True,
        "flight": flight,
        "issue": issue,
        "alternatives": alternatives,
        "recommendations": recommendations,
    }
