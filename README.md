# 🍱 Food Donation Platform

A role-based web application designed to connect food donors with people in need, helping reduce food waste and support communities.

---

## 🚀 Live Features

### 🔐 Authentication
- Secure Login & Signup system
- Role-based access control

### 👤 User Roles

#### 👑 Admin
- View total donations, requests, and users
- Access admin dashboard with recent activity
- Monitor overall system

#### 🍛 Donor
- Add food donations
- View personal donation history

#### 🙋 Receiver
- Request food
- View all food requests

---

## 📊 Dashboard Highlights

- Total Donations Count  
- Total Requests Count  
- Total Users  
- Recent Donations & Requests  

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|------------|------------------|
| Frontend   | HTML, CSS        |
| Backend    | Flask (Python)   |
| Database   | SQLite           |
| Deployment | Railway          |

---

## 📂 Project Structure

├── static/
│ ├── style.css
│ └── images/
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── signup.html
│ ├── donate.html
│ ├── request.html
│ ├── donations.html
│ ├── requests.html
│ └── admin.html├── app.py
├── requirements.txt
└── README.md


---

## 🔑 Key Functionalities

- Role-based redirection after login  
- Session handling for authentication  
- Food donation and request system  
- Admin analytics dashboard  
- Clean and responsive UI  

---

## ⚠️ Important Note

- This project uses SQLite for simplicity  
- Data may reset on deployment platforms like Railway  

---

## 💡 Future Enhancements

- PostgreSQL integration (persistent database)  
- Live location-based food tracking (map integration)  
- Notification system  
- Food pickup scheduling  
- Image upload for donations  

---

## 🎯 Project Goal

To build a simple yet impactful platform that:
- Reduces food waste  
- Helps people in need  
- Demonstrates full-stack development skills  

---

## 👩‍💻 Author

**Neha Wadhwa**

---
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


## ⚠️ Note

Data may reset occasionally due to deployment environment.  
If login fails, please create a new account using Signup.


## 🌐 Live Demo
https://food-donation-platform-production-91c9.up.railway.app/