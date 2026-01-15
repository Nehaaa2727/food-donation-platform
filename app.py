from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method =='POST':
        name = request.form['name']
        food_item = request.form['food_item']
        quantity = request.form['quantity']
        location = request.form['location']

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

        return "Food donated successfully!"
    return render_template('donate.html')
        
if __name__ == "__main__":
    app.run(debug=True)