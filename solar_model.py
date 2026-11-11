# solar_model.py (Fake Student C)

def predict_solar(weather_json):
    print("Running fake solar LSTM model...")
    
    # In reality, Student C will feed weather_json into their LSTM model.
    # For now, we just return a fake prediction.
    return {
        "status": "success",
        "source": "solar",
        "unit": "MW",
        "forecast": [
            {"timestamp": "2026-11-11T12:00:00Z", "predicted_power_MW": 0.45},
            {"timestamp": "2026-11-11T13:00:00Z", "predicted_power_MW": 0.55},
            {"timestamp": "2026-11-11T14:00:00Z", "predicted_power_MW": 0.30}
        ]
    }
