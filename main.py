from fastapi import FastAPI
# Import the fake modules we just made
from weather_module import get_weather
from wind_model import predict_wind
from solar_model import predict_solar

app = FastAPI()

# 1. A simple test endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Renewable Forecast API!"}

# 2. The main endpoint that connects A, B, and C
@app.get("/api/forecast")
def get_forecast(location: str = "Toronto"):
    # Step A: Get weather data
    weather_data = get_weather(location)
    
    # Step B: Pass weather to Wind model
    wind_data = predict_wind(weather_data)
    
    # Step C: Pass weather to Solar model
    solar_data = predict_solar(weather_data)
    
    # Step D: Combine everything and send it out
    return {
        "location": location,
        "weather": weather_data,
        "wind_forecast": wind_data,
        "solar_forecast": solar_data
    }
