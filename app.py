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
    user_id INTEGER,
    name TEXT,
    food_item TEXT,
    quantity TEXT,
    location TEXT,
    latitude REAL,
    longitude REAL
)
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receiver_name TEXT,
    food_needed TEXT,
    quantity TEXT,
    location TEXT,
    user_id INTEGER
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
    if 'role' in session:
        if session['role'] == 'admin':
            return redirect('/admin')
        elif session['role'] == 'donor':
            return redirect('/donate')
        else:
            return redirect('/request')

    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        # ✅ Validation
        if not name or not email or not password or not role:
            flash("All fields are required", "error")
            return redirect('/signup')

        if len(password) < 4:
            flash("Password must be at least 4 characters", "error")
            return redirect('/signup')

        conn = get_connection()
        cursor = conn.cursor()

        # ✅ Check duplicate email
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        existing = cursor.fetchone()

        if existing:
            conn.close()
            flash("Email already exists", "error")
            return redirect('/signup')

        # ✅ Insert user
        cursor.execute("""
            INSERT INTO users (name, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (name, email, password, role))

        conn.commit()
        conn.close()

        flash("Signup successful! Please login.", "success")
        return redirect('/login')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # ✅ Validation
        if not email or not password:
            flash("Please fill all fields", "error")
            return redirect('/login')

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
            session['name'] = user[1]
            session['role'] = user[4]

            # ✅ Role-based redirect
            if user[4] == 'admin':
                return redirect('/admin')
            elif user[4] == 'donor':
                return redirect('/donate')
            else:
                return redirect('/request')

        else:
            session.clear()   # 🔥 ADD THIS LINE
            flash("Invalid credentials", "error")
            return redirect('/login')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/admin')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    # Counts
    cursor.execute("SELECT COUNT(*) FROM donors")
    total_donations = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM receivers")
    total_requests = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # 🔥 NEW: Recent donations
    cursor.execute("SELECT * FROM donors ORDER BY id DESC LIMIT 3")
    recent_donations = cursor.fetchall()

    # 🔥 NEW: Recent requests
    cursor.execute("SELECT * FROM receivers ORDER BY id DESC LIMIT 3")
    recent_requests = cursor.fetchall()

    conn.close()

    return render_template(
        'admin.html',
        total_donations=total_donations,
        total_requests=total_requests,
        total_users=total_users,
        recent_donations=recent_donations,
        recent_requests=recent_requests
    )
# ---------------- DONATE ----------------
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    # ✅ ROLE CHECK FIRST
    if session.get('role') != 'donor':
      return redirect('/login')

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
INSERT INTO donors (user_id, name, food_item, quantity, location, latitude, longitude)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    session['user_id'], name, food_item, quantity, location, latitude, longitude
))

        conn.commit()
        conn.close()

        flash("Donation added successfully!", "success")
        return redirect('/donations')

    return render_template('donate.html')


# ---------------- DONATIONS ----------------
@app.route('/donations')
def donations():
    if session.get('role') != 'donor':
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM donors WHERE user_id=?",
        (session['user_id'],)
    )

    data = cursor.fetchall()
    conn.close()

    return render_template('donations.html', donations=data)


# ---------------- REQUEST FOOD ----------------
@app.route('/request', methods=['GET', 'POST'])
def request_food():
    if session.get('role') != 'receiver':
      return redirect('/login')

    if request.method == 'POST':
        receiver_name = request.form['receiver_name']
        food_needed = request.form['food_needed']
        quantity = request.form['quantity']
        location = request.form['location']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO receivers (receiver_name, food_needed, quantity, location, user_id)
            VALUES (?, ?, ?, ?, ?)
        """, (receiver_name, food_needed, quantity, location, session['user_id']))

        conn.commit()
        conn.close()

        flash("Request added successfully!", "success")
        return redirect('/requests')

    return render_template('request.html')


# ---------------- VIEW REQUESTS ----------------
@app.route('/requests')
def view_requests():
    if 'role' not in session:
        return redirect('/login')

    conn = get_connection()
    cursor = conn.cursor()

    if session['role'] == 'admin':
        cursor.execute("SELECT * FROM receivers")

    elif session['role'] == 'receiver':
        cursor.execute("SELECT * FROM receivers WHERE user_id=?", (session['user_id'],))

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