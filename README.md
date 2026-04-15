1. Title:-Smart Crop Recommendation System using AI & Django
   
2. Description:-This project is an AI-powered web application developed using Django that recommends the most suitable crop based on soil parameters and environmental conditions. It uses a machine learning model to analyze inputs such as nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall to generate accurate crop predictions. The system helps farmers make data-driven decisions for better agricultural productivity.

3. Features
AI/ML-based crop prediction system

Takes soil and environmental parameters as input

Real-time prediction results using trained model

User-friendly web interface built with Django

5. Tech Stack
Python
Django
Random forest(ML Model)
HTML, CSS, JavaScript
SQLite (Database)
Pandas, NumPy (Data processing)

6. Installation Steps
git clone <your-repository-url>
cd smart-crop-recommendation
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
