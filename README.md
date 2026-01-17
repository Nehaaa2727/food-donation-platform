# 🍱 Food Donation Platform

A web-based application built using **Flask and MySQL** that helps connect people who want to donate surplus food with those who need it.

This project focuses on solving a real-world problem while following clean backend and frontend practices.

---

## 🚀 Features

- Donate food with details (name, food item, quantity, location)
- Request food from donors
- View all donations in a structured table
- View donation locations on an interactive map
- Flash messages for success and error feedback
- Clean and user-friendly UI
- Secure database handling using parameterized queries

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Jinja2  
- **Database:** MySQL  
- **Maps:** Leaflet + OpenStreetMap  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure

food-donation-platform/
│
├── app.py
├── db.py
├── requirements.txt
├── README.md
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── donate.html
│ ├── donations.html
│ ├── request.html
│ ├── requests.html
│ └── map.html
│
└── static/
└── style.css

2. Install dependencies
pip install -r requirements.txt

3.Configure MySQL database:
.Create database
.Create required tables
.Update credentials in db.py

4. Run the app:
python app.py

5. open browser:
http://127.0.0.1:5000/
