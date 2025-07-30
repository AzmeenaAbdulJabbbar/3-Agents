from agents import function_tool
from typing_extensions import TypedDict  

class FlightData(TypedDict):
    departure: str
    destination: str
    date: str

@function_tool
async def get_flights(input: FlightData) -> dict:
    departure_city = input["departure"]
    destination_city = input["destination"]
    travel_date = input["date"]  # ✅ Corrected ke

    # Mock flight data
    available_flights = [
        {"airline": "Air Blue", "departure time": "08:00 AM", "arrival time": "10:00 AM", "price": "30000 PKR"},
        {"airline": "PIA", "departure time": "10:00 AM", "arrival time": "7:00 PM", "price": "80000 PKR"},
        {"airline": "Shaheen Airline", "departure time": "02:00 PM", "arrival time": "5:00 PM", "price": "25000 PKR"}
    ]

    return {
        "flights": available_flights, 
        "route": f"{departure_city} -> {destination_city}",
        "date": travel_date
    }
