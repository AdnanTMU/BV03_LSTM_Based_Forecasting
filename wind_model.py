# wind_model.py (Fake Student B)

def predict_wind(weather_json):
    print("Running fake wind LSTM model...")
    
    # In reality, Student B will feed weather_json into their LSTM model.
    # For now, we just return a fake prediction.
    return {
        "status": "success",
        "source": "wind",
        "unit": "MW",
        "forecast": [
            {"timestamp": "2026-11-11T12:00:00Z", "predicted_power_MW": 0.65},
            {"timestamp": "2026-11-11T13:00:00Z", "predicted_power_MW": 0.72},
            {"timestamp": "2026-11-11T14:00:00Z", "predicted_power_MW": 0.81}
        ]
    }
