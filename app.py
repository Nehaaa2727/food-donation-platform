from flask import Flask, render_template, request, redirect, url_for, flash
from db import get_connection


app = Flask(__name__)
app.secret_key = "food_donation_secret"

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
        
        if not name or not food_item or not quantity or not location:
            flash("All fields are required!", "error")
            return redirect(url_for('donate'))
        
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO donors (name, food_item, quantity, location)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, food_item, quantity, location))
        conn.commit()

        cursor.close()
        conn.close()

        flash("Food donated successfully!", "success")
        return redirect(url_for('donate'))

    return render_template('donate.html')


@app.route('/donations')
def donations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

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

        if not receiver_name or not food_needed or not quantity or not location:
            return "Please fill all fields"

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO receivers (receiver_name, food_needed, quantity, location)
        VALUES (%s, %s, %s, %s)
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
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM receivers")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('requests.html', requests=data)

@app.route('/map')
def map_view():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT latitude, longitude 
        FROM donors 
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
    """)
    donors = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('map.html', donors=donors)




if __name__ == "__main__":
    app.run()