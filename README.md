# BV03_LSTM_Based_Forecasting
This capstone project focuses on developing a cloud-hosted, modular forecasting system for renewable energy generation. The primary objective is to utilize Long Short-Term Memory (LSTM) neural networks to predict the power output of representative 1 MW wind and solar systems based on forecasted weather data.

Github Structure:

├── main.py                  <-- FastAPI backend (The "Brain")

├── weather_module.py        <-- Student A

├── wind_model.py            <-- Student B (LSTM model will be stored in GCP)

├── solar_model.py           <-- Student C (LSTM model will be stored in GCP)

├── templates/               <-- UI Codes

│   └── index.html           <-- The actual webpage (HTML/CSS layout)

├── requirements.txt         <-- Libraries

└── Dockerfile               <-- Communication with GCP
