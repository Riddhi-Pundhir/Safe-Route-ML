# 🚀 SafeRoute AI – Intelligent Safety-Based Navigation System

SafeRoute AI is a machine learning-based prototype system that predicts the safety level of a route using contextual factors such as environmental conditions, time-based risk, and modeled crime-related patterns. It is designed to help users make more informed route decisions beyond just speed or distance.

---

## 🌍 Problem Statement

Most navigation systems optimize for speed or distance but ignore safety.

SafeRoute AI introduces:
- Safety-aware navigation
- Risk-based route classification
- Context-driven decision support

---

## 🧠 Machine Learning Approach

### 🔹 Features Used
- Latitude & Longitude
- Modeled crime severity (derived from dataset patterns)
- Lighting conditions (day/night approximation)
- Crowd density (simulated)
- Hour of the day

### 🔹 Risk Scoring
A weighted scoring system is used:
- Crime-related severity → 50%
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

- Achieved high accuracy (~97%) on the processed dataset used for experimentation  
- Strong performance across:
  - Precision  
  - Recall  
  - F1 Score  

- Classifies routes into:
  - Safe  
  - Moderate Risk  
  - High Risk  

---

## ⚙️ System Architecture

User Input → Google Maps → FastAPI Backend → ML Model → Safety Prediction → UI Display

---

## 💻 Tech Stack

### Backend
- Python  
- FastAPI  

### Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  

### Frontend
- HTML, CSS, JavaScript  
- Google Maps API  

---

## 🔄 How It Works

1. User enters start and destination  
2. Google Maps generates route data  
3. Coordinates and time are extracted  
4. Data is sent to backend  
5. ML model predicts safety level  
6. Result is displayed in the UI  

---

## 📁 Project Structure

- `app.py` → FastAPI backend  
- `ustm.py` → Model training  
- `ust_model.pkl` → Trained model  
- `index.html` → Frontend  
- `style.css` → Styling  
- `fnm.js` → Frontend logic  
- `crime_safety_dataset.csv`  
- `crime_safety_processed.csv`  

---

## ⚠️ Disclaimer

This project is a prototype developed for educational and research purposes. It uses simulated and processed datasets and does not represent real-time or authoritative safety data.

The system provides indicative safety insights based on modeled factors and should not be used as a sole source for real-world decision-making.

---

## ⚙️ Setup Instructions

1. Install dependencies:
   pip install fastapi uvicorn scikit-learn pandas numpy joblib

2. Run backend:
   uvicorn app:app --reload
   
3. Open `index.html` in browser  

---

## 🔑 API Key Note

Replace the placeholder in `index.html`:

YOUR_API_KEY_HERE

with your own Google Maps API key.

---

## 🚀 Future Improvements

- Integration with openly licensed public datasets (subject to permissions)  
- Multi-route safety comparison with dynamic scoring  
- Improved feature engineering (weather, population density, etc.)  
- Deployment with scalable backend infrastructure  
- Mobile-friendly interface  

---

## 🎯 Key Highlights

This project demonstrates:
- End-to-end ML system design  
- Feature engineering  
- API integration  
- Full-stack development  
- Consideration of ethical and data-related constraints  

---

## 📌 Summary

SafeRoute AI is a practical prototype that combines machine learning and contextual signals to provide safer navigation insights, with a focus on usability, scalability, and responsible data usage.
