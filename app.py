from dbm import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash , session
from db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ✅ Donors table
    cursor.execute("""
  CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    food_item TEXT,
    quantity TEXT,
    location TEXT,
    latitude REAL,
    longitude REAL,
    user_id INTEGER
)
""")

    # ✅ Receivers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receiver_name TEXT,
        food_needed TEXT,
        quantity TEXT,
        location TEXT
    )
    """)

    # ✅ Users table (NEW)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()


app = Flask(__name__)
app.secret_key = "food_donation_secret"
create_tables()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (name, email, password, role)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['role'] = user[4]

            if user[4] == 'admin':
                return redirect('/admin')
            elif user[4] == 'donor':
                return redirect('/donate')
            else:
                return redirect('/request')

        return "Invalid credentials"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
@app.route('/admin')
def admin_dashboard():
    if 'role' not in session or session['role'] != 'admin':
        return "Access Denied"

    return render_template('admin.html')
# ---------------- DONATE ----------------
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    # ✅ ROLE CHECK FIRST
    if session.get('role') != 'donor':
        return redirect('/')

    if request.method == 'POST':
        name = request.form['name']
        food_item = request.form['food_item']
        quantity = request.form['quantity']
        location = request.form['location']

        latitude = 28.9845
        longitude = 77.7064

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO donors (name, food_item, quantity, location, latitude, longitude)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, food_item, quantity, location, latitude, longitude))

        conn.commit()
        conn.close()

        flash("Donation added successfully!", "success")
        return redirect('/donations')

    return render_template('donate.html')


# ---------------- DONATIONS ----------------
@app.route('/donations')
def donations():
    if 'role' not in session:
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    # ✅ ADMIN sees all
    if session['role'] == 'admin':
        cursor.execute("SELECT * FROM donors")

    # ✅ DONOR sees only their data (by name for now)
    elif session['role'] == 'donor':
           cursor.execute("SELECT * FROM donors")

    else:
        return "Access Denied"

    data = cursor.fetchall()
    conn.close()

    return render_template('donations.html', donations=data)


# ---------------- REQUEST FOOD ----------------
@app.route('/request', methods=['GET', 'POST'])
def request_food():
    # ✅ ROLE CHECK FIRST
    if session.get('role') != 'receiver':
        return redirect('/')

    if request.method == 'POST':
        receiver_name = request.form['receiver_name']
        food_needed = request.form['food_needed']
        quantity = request.form['quantity']
        location = request.form['location']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO receivers (receiver_name, food_needed, quantity, location)
            VALUES (?, ?, ?, ?)
        """, (receiver_name, food_needed, quantity, location))

        conn.commit()
        conn.close()

        flash("Request submitted successfully!", "success")
        return redirect('/requests')

    return render_template('request.html')


# ---------------- VIEW REQUESTS ----------------
@app.route('/requests')
def view_requests():
    if 'role' not in session:
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    # ✅ ADMIN sees all
    if session['role'] == 'admin':
        cursor.execute("SELECT * FROM receivers")

    # ✅ RECEIVER sees only their requests
    elif session['role'] == 'receiver':
        cursor.execute("SELECT * FROM receivers WHERE receiver_name=?", (session.get('name'),))

    else:
        return "Access Denied"

    data = cursor.fetchall()
    conn.close()

    return render_template('requests.html', requests=data)
#@app.route('/map')
#def map_view():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    rows = cursor.fetchall()

    donors = [dict(row) for row in rows]

    conn.close()

    return render_template('map.html', donors=donors)


if __name__ == "__main__":
    create_tables()   # 👈 ADD THIS LINE
    app.run()