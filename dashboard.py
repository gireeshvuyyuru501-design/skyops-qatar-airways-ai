import requests
import streamlit as st


st.set_page_config(page_title="SkyOps AI", page_icon="✈️", layout="wide")
st.title("✈️ SkyOps AI")
st.caption("Qatar Airways-inspired airline operations demo — unofficial portfolio project.")

api = st.sidebar.text_input("FastAPI URL", "http://127.0.0.1:8000")

tab1, tab2, tab3 = st.tabs(["Flight Search", "Passenger Assistant", "Disruption Desk"])

with tab1:
    c1, c2 = st.columns(2)
    origin = c1.text_input("Origin", "DOH")
    destination = c2.text_input("Destination", "JFK")
    if st.button("Search Flights"):
        r = requests.post(
            f"{api}/flights/search",
            json={"origin": origin, "destination": destination},
            timeout=20,
        )
        r.raise_for_status()
        st.json(r.json())

with tab2:
    question = st.text_area(
        "Passenger question",
        "What should I know about baggage allowance?",
    )
    if st.button("Ask SkyOps"):
        r = requests.post(
            f"{api}/assist",
            json={"question": question, "passenger_name": "Demo Passenger"},
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        st.subheader("Answer")
        st.write(data["answer"])
        st.write("**Sources:**", ", ".join(data["sources"]))
        st.write("**Recommended actions:**")
        for item in data["action_recommendations"]:
            st.write("•", item)

with tab3:
    flight_number = st.text_input("Flight number", "QR739")
    issue = st.text_input("Issue", "Passenger may miss onward connection due to delay")
    if st.button("Analyze Disruption"):
        r = requests.post(
            f"{api}/disruption",
            json={"flight_number": flight_number, "issue": issue},
            timeout=20,
        )
        r.raise_for_status()
        st.json(r.json())
