# 🌧️ Rainfall Prediction Web App (2017–2026)

This is a Flask-based web application that predicts monthly rainfall for the years **2025** and **2026** based on **Indian state and district** input. It uses historical rainfall data from **2017 to 2023** to make accurate predictions using a trained machine learning model.

## 🚀 Features

- 📍 Select State and District
- 📅 Predict month-wise rainfall for 2025 and 2026
- 📊 Interactive graphs and visualizations
- 📥 Download rainfall reports as CSV or PDF
- 🌐 Simple and responsive web UI

---

## 🧠 ML Model Details

- **Model:** `rainfall_monthly_model.pkl`
- **Encoders:** 
  - `state_encoder.pkl`
  - `district_encoder.pkl`
- **Input Features:** Encoded state, encoded district, and 16 numerical weather parameters.

---

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/rainfall-prediction.git
   cd rainfall-prediction

2.Create virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`

3.Install dependencies:

bash
Copy code
pip install -r requirements.txt

4.Run the Flask app:

bash
Copy code
python app.py


📁 Project Structure
rainfall-prediction/
├── app.py
├── rainfall_monthly_model.pkl
├── state_encoder.pkl
├── district_encoder.pkl
├── Rainfall_Data_2017_2023.csv
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── style.css
│   └── charts.js
└── requirements.txt
)

📌 To-Do
Add support for multi-year predictions

Improve UI with real-time weather integration

Add authentication (future feature)

🙋‍♀️ Author
Rutuja Gaikwad
Final Year B.Tech (CSE)
SVERI's College of Engineering, Pandharpur


