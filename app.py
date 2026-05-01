from dbm import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # RESET TABLE (important for fix)
    cursor.execute("DROP TABLE IF EXISTS donors")

    cursor.execute("""
    CREATE TABLE donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        food_item TEXT,
        quantity TEXT,
        location TEXT,
        latitude REAL,
        longitude REAL
    )
    """)

    cursor.execute("DROP TABLE IF EXISTS receivers")

    cursor.execute("""
    CREATE TABLE receivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receiver_name TEXT,
        food_needed TEXT,
        quantity TEXT,
        location TEXT
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



@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form['name']
        food_item = request.form['food_item']
        quantity = request.form['quantity']
        location = request.form['location']

        # ✅ ADD THIS (IMPORTANT)
        latitude = 28.9845
        longitude = 77.7064

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO donors (name, food_item, quantity, location, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(query, (name, food_item, quantity, location, latitude, longitude))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('donations'))

    return render_template('donate.html')


@app.route('/donations')
def donations():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM donors"
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('donations.html', donations=data)

@app.route('/request', methods=['GET', 'POST'])
def request_food():
    if request.method == 'POST':
        receiver_name = request.form['receiver_name']
        food_needed = request.form['food_needed']
        quantity = request.form['quantity']
        location = request.form['location']
        latitude = 28.9845
        longitude = 77.7064

        if not receiver_name or not food_needed or not quantity or not location:
            return "Please fill all fields"

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO receivers (receiver_name, food_needed, quantity, location)
        VALUES (?, ?, ?, ?)


        """
        cursor.execute(query, (receiver_name, food_needed, quantity, location))
        conn.commit()

        cursor.close()
        conn.close()
        flash("Food request submitted successfully!", "success")
        return redirect(url_for('request_food'))


  

    return render_template('request.html')

@app.route('/requests')
def view_requests():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM receivers")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('requests.html', requests=data)

@app.route('/map')
def map_view():
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