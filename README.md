# SkyOps AI ✈️

**Qatar Airways-inspired Airline Operations & Passenger Assistance Demo**

> Unofficial portfolio project. Not affiliated with, endorsed by, or connected to Qatar Airways.

## What it demonstrates

SkyOps AI models real airline workflows using simulated data:

- Flight search
- Passenger policy assistance
- Disruption handling
- Alternative itinerary recommendations
- Human-in-the-loop rebooking controls
- FastAPI / Swagger
- Streamlit operations dashboard
- OpenAI integration with a no-key local fallback
- PyTest
- Docker
- GitHub Actions

## Architecture

```text
Passenger / Operations User
          ↓
       FastAPI
          ↓
 ┌───────────────────┐
 │ Flight Search     │
 │ Policy Retrieval  │
 │ Disruption Logic  │
 │ OpenAI Assistant  │
 └───────────────────┘
          ↓
 Human Confirmation Layer
          ↓
 Recommendation / Action Plan
```

## Run in one shot

```powershell
cd C:\AI\skyops-qatar-airways-ai
Set-ExecutionPolicy -Scope Process Bypass -Force
Unblock-File .\run_all.ps1
Unblock-File .\run_dashboard.ps1
.\run_all.ps1
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

The project works **without an OpenAI key** using a deterministic local fallback.

To enable OpenAI, edit `.env`:

```env
OPENAI_API_KEY=YOUR_OPENAI_KEY
OPENAI_MODEL=gpt-4.1-mini
```

## Swagger demos

### Flight search

`POST /flights/search`

```json
{
  "origin": "DOH",
  "destination": "JFK"
}
```

### Passenger assistant

`POST /assist`

```json
{
  "question": "What should I know about baggage allowance?",
  "passenger_name": "Demo Passenger"
}
```

### Disruption desk

`POST /disruption`

```json
{
  "flight_number": "QR739",
  "issue": "Passenger may miss onward connection due to delay"
}
```

### Evaluation

`POST /evaluate`

Expected:

```text
5 / 5 passed
```

## Dashboard

Second terminal:

```powershell
cd C:\AI\skyops-qatar-airways-ai
Set-ExecutionPolicy -Scope Process Bypass -Force
.\run_dashboard.ps1
```

Open:

```text
http://localhost:8501
```

## GitHub description

```text
Qatar Airways-inspired airline operations AI demo with FastAPI, OpenAI, disruption intelligence, policy retrieval, Streamlit, Docker, PyTest, and CI/CD.
```

## Suggested topics

```text
airline-ai
travel-ai
openai
fastapi
generative-ai
agentic-ai
streamlit
docker
pytest
github-actions
python
airline-operations
```

## Resume bullets

- Built a Qatar Airways-inspired airline operations AI demo using FastAPI, OpenAI, simulated flight data, and policy retrieval for passenger assistance and disruption workflows.
- Implemented flight search, disruption analysis, alternative-itinerary recommendations, and human-in-the-loop controls for consequential booking actions.
- Developed a Streamlit operations dashboard, automated PyTest validation, Docker packaging, and GitHub Actions CI/CD.

## Author

Girish Vuyyuru

- GitHub: https://github.com/gireeshvuyyuru501-design
- LinkedIn: https://www.linkedin.com/in/girish-genai-engineer
- Portfolio: https://gireeshvuyyuru501-design.github.io/Launch-AI-engineering-portfolio/

## Disclaimer

This repository is a personal educational/portfolio project using simulated data. It is not an official Qatar Airways application and does not provide real booking, ticketing, flight-status, or rebooking services.
