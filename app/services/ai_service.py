from openai import OpenAI
from app.config import get_settings


SYSTEM = """You are SkyOps AI, an airline operations and passenger-assistance demo.

Rules:
- This is an unofficial portfolio project and not an official Qatar Airways system.
- Use only the supplied simulated flight and demo policy context.
- Never claim a booking or rebooking actually happened.
- For consequential actions, recommend human confirmation.
- Be concise and operational.
"""


def generate_answer(question: str, context: str) -> tuple[str, str]:
    settings = get_settings()

    if not settings.openai_api_key:
        fallback = (
            "Based on the simulated airline data and demo policy context: "
            f"{context} Human confirmation is required before any booking, "
            "rebooking, refund, or special-service action."
        )
        return fallback, "local-fallback"

    client = OpenAI(api_key=settings.openai_api_key)
    response = client.responses.create(
        model=settings.openai_model,
        instructions=SYSTEM,
        input=f"Question:\n{question}\n\nContext:\n{context}",
    )
    return response.output_text, settings.openai_model
