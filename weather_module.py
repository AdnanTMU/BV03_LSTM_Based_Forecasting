# weather_module.py (Fake Student A)

def get_weather(location):
    print(f"Fetching fake weather for {location}...")
    
    # We are returning a dictionary that mimics the JSON contract we agreed on
    return {
        "status": "success",
        "location": location,
        "forecast": [
            {"timestamp": "2026-11-11T12:00:00Z", "wind_speed_mps": 6.5, "temperature_C": 15.0},
            {"timestamp": "2026-11-11T13:00:00Z", "wind_speed_mps": 7.2, "temperature_C": 15.5},
            {"timestamp": "2026-11-11T14:00:00Z", "wind_speed_mps": 8.1, "temperature_C": 16.0}
        ]
    }
