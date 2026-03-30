# 🚀 SafeRoute AI – Intelligent Safety-Based Navigation System

SafeRoute AI is a machine learning-based system that predicts the safety level of a route using real-world factors like crime data, environmental conditions, and time-based risk.
It is designed to help users choose safer routes instead of just the shortest or fastest ones.

---

## 🌍 Problem Statement

Most navigation systems optimize for speed or distance but ignore safety.

SafeRoute AI introduces:
- Safety-aware navigation
- Risk-based route classification
- Intelligent decision-making using machine learning

---

## 🧠 Machine Learning Approach

### 🔹 Features Used
- Latitude & Longitude
- Crime severity (derived from crime type)
- Lighting conditions (day/night)
- Crowd density
- Hour of the day

### 🔹 Risk Scoring
A weighted scoring system is used:
- Crime Severity → 50%
- Lighting → 25%
- Crowd Density → 15%
- Time-based risk → 10%

### 🔹 Models Trained
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting (Final Model)

### 🔹 Final Model
- Gradient Boosting Classifier

---

## 📊 Results

- Achieved ~97% accuracy using Gradient Boosting Classifier
- Strong performance across:
  - Precision
  - Recall
  - F1 Score

- Classifies routes into:
  - Safe
  - Moderate Risk
  - High Risk
  - Enables visual comparison of multiple route safety levels

---

## ⚙️ System Architecture

User Input → Google Maps → FastAPI Backend → ML Model → Safety Prediction → UI Display

---

## 💻 Tech Stack

**Backend**
- Python
- FastAPI

**Machine Learning**
- Scikit-learn
- Pandas
- NumPy

**Frontend**
- HTML, CSS, JavaScript
- Google Maps API

---

## 🔄 How It Works

1. User enters start and destination
2. Google Maps generates route data
3. Coordinates + time extracted
4. Data sent to backend
5. ML model predicts safety
6. Result shown in UI

---

## 📁 Project Structure

- app.py → FastAPI backend
- ustm.py → Model training
- ust_model.pkl → Trained model
- index.html → Frontend
- style.css → Styling
- fnm.js → Frontend logic
- crime_safety_dataset.csv
- crime_safety_processed.csv

---

## ⚠️ Setup Instructions

1. Install dependencies:
   pip install fastapi uvicorn scikit-learn pandas numpy joblib

2. Run backend:
   uvicorn app:app --reload

3. Open index.html in browser

---

## 🔑 API Key Note

Replace this in index.html:

YOUR_API_KEY_HERE

with your own Google Maps API key.

---

## 🚀 Future Improvements

- Integration with publicly available or open crime datasets for improved real-world accuracy
- Enhanced multi-route safety comparison with dynamic scoring
- Improved feature engineering using additional contextual signals (weather, population density, etc.)
- Deployment as a web service with scalable backend support
- Extension to mobile-friendly interface for wider accessibility

---

## 🎯 Key Highlight

This project demonstrates:
- End-to-end ML system design
- Feature engineering
- API integration
- Full-stack development
