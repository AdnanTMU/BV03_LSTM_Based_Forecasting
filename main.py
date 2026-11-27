from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Mock modules for Students A, B and C
from weather_module import get_weather
from wind_model import predict_wind
from solar_model import predict_solar

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/api/forecast")
def get_forecast(location: str = "Toronto"):
    # Step A: get weather data
    weather_data = get_weather(location)

    # Step B: pass weather to the wind model
    wind_data = predict_wind(weather_data)

    # Step C: pass weather to the solar model
    solar_data = predict_solar(weather_data)

    # Step D: combine everything and send it out
    return {
        "location": location,
        "weather": weather_data,
        "wind_forecast": wind_data,
        "solar_forecast": solar_data,
    }

@app.get("/", response_class=HTMLResponse)
def serve_ui(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
