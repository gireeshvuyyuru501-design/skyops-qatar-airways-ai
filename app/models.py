from pydantic import BaseModel, Field


class FlightSearchRequest(BaseModel):
    origin: str = Field(min_length=3, max_length=3)
    destination: str = Field(min_length=3, max_length=3)


class AssistRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)
    passenger_name: str = "Demo Passenger"


class DisruptionRequest(BaseModel):
    flight_number: str
    issue: str = Field(min_length=3, max_length=500)


class Flight(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure: str
    arrival: str
    status: str
    cabin: str


class AssistResponse(BaseModel):
    answer: str
    sources: list[str]
    action_recommendations: list[str]
    model_used: str
