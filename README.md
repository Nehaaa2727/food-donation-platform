🍱 Food Donation Platform

A web-based application that helps connect food donors with people or organizations in need.
This project is built using Flask, SQLite, HTML, CSS, and focuses on solving the real-world problem of food wastage.

🚀 Project Objective
The main goal of this project is to:
.Reduce food wastage
.Allow users to donate surplus food easily
.Maintain a record of all food donations
.View donation locations on a map

🛠️ Tech Stack Used
.Backend: Python (Flask)
.Database: SQLite3
.Frontend: HTML, CSS, Jinja2
.Maps: Leaflet.js + OpenStreetMap
.Version Control: Git & GitHub
.Deployment: Render

📁 Project Structure
food-donation-platform/
│
├── app.py
├── db.py
├── food.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── donate.html
│   ├── donations.html
│   ├── map.html
│   ├── request.html
│   └── requests.html
│
└── static/
    └── style.css

⚙️ Features
.🥗 Donate food using a simple form
.📋 View all donated food entries
.🗺️ View donation locations on an interactive map
.📦 Request food (basic implementation)
.🎨 Clean UI with navigation buttons (no manual URL typing)

🧠 What I Learned From This Project
.How Flask routing works
.Connecting Flask with SQLite database
.Difference between MySQL and SQLite query placeholders (%s vs ?)
.Using Jinja2 templates
.Handling form data using POST requests
.Debugging common Flask & SQL errors
.Deploying a Flask application on Render
.Using GitHub properly for version contro

▶️ How to Run Locally
1.Clone the repository
git clone https://github.com/Nehaaa2727
/food-donation-platform.git
2.Install depemdmcies
pip install -r requirements.txt
3.Run the app
python app.py
4.Open browser
http://127.0.0.1:5000/
