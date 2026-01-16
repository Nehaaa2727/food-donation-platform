###Food Donation Platform

##DAY 1 goal
-set up project foundation using flask , MySQL, and GitHub

##what i did?
-created project folder and opened it in vs code
-set up basic flask application(app.py)
-ran flask server successfully
-created MySQL database: food_donation_db
-designed tables: users, food_posts, requests
-created MySQL connection(db.py)
-added project dependencies in requirements.txt
-initialize git and pushed code to GitHub

##files and their purpose?
-app.py: main flask app(routes and server)
-db.py: handles MySQL database connection
-requirements.txt: lists python package used
-templates/ : HTML files(future use)
-static/ : CSS AND JS files

##key concepts
-flask app structure
-how backend connects to MySQL 
-basic database design
-GitHub version control(init, commit, push)

##imp commands
-python app.py
-git init
-git add
-git commit -m "day 1 commit"
-git push

##problem faced and fixed
-git remote url error
-fixed using git remote set-url


Day 2:
• Created Flask app structure
• Understood templates and static folders
• Created MySQL database and donor table
• Learned how Flask connects to MySQL using db.py

• Flask automatically looks for HTML files inside templates folder
• static folder is used for CSS, JS, images
• db.py is used to keep database code separate from app.py

(Flask → framework

render_template → HTML file browser me show karne ke liye

__name__ → Flask ko batata hai ki yahi main app hai) Flask(__name__) tells Flask where the app is running from
. A route maps a URL to a Python function
.debug mode helps during development
.HTML files are rendered using render_template()

def get_connection():
bar bar connection code repeat na karna pade
clean code rahe
.Database connection code is separated to improve security and maintainability



DAY 3
#Frontend (HTML Form)
.A donation form is created using HTML.
.The form collects donor name, food item, quantity, and location.
.The form uses the POST method to send data securely

#Flask Route for Donation
.A /donate route is created.
.It handles both GET and POST requests.
.GET request loads the donation form.
.POST request processes the form data.

#Handling Form Data in Flask
.Flask provides request.form to access submitted form values.
.Each input field is accessed using its name attribute.

#Database Insertion (MySQL)
.A database connection is created using a separate file (db.py).
.SQL INSERT query is used to store donor details.
.Connection and cursor are closed after insertion.

#Error Handling & Debugging
.Flask server must be restarted after code changes.
.All routes must be defined before app.run().
.Correct database credentials are required.

#Output Verification
.Success message is displayed after form submission.
.Data is verified using SELECT query in MySQL

DAY 4
1. Viewing Donations from Database
I created a new route /donations in Flask to fetch all donation records from the MySQL database and show them on a webpage.
Key learning:
.Flask can send database data to HTML templates
.render_template() is used to pass data to frontend

2. Fetching Data from MySQL
 used MySQL connector with dictionary=True so that database rows behave like dictionaries.
 .Makes data easy to access in HTML using column names
.Prevents index-based confusion

3. Jinja Template Usage
In donations.html, I used Jinja templating to loop over the data.
.{% for %} → used for looping
.{{ }} → used to display data
.Used dictionary style access: d['column_name']

4. Adding CSS Styling
created a style.css file inside the static folder to improve UI.
.Flask serves static files using url_for()
.CSS improves readability and structure


DAY 5
1. Understanding Real-World Flow
In real life, food donation works in two directions:
.Donors provide food
.NGOs or receivers request food
To represent this flow, a separate receiver module was created.

2. Receiver Database Table
A new table receivers was created in MySQL to store food requests.
Fields:
.receiver_name
.food_needed
.quantity
.location
This separation keeps donor and receiver data organized.

3. Receiver Request Feature
A new route /request was added where NGOs can submit food requests using a form.
Key points:
.Uses POST method
.Data is validated before insertion
.Data is stored securely in MySQL
This ensures incomplete requests are not stored.

4. Viewing Receiver Requests
A separate route /requests was created to display all food requests.
Purpose:
.Donors or admins can view NGO requirements
.Uses GET method
.Fetches data from database and displays in table format

5. Difference Between Submitting and Viewing Requests
Although both features use the same table:
.Request submission inserts data
.Request viewing retrieves data
This separation follows good backend design principle

6. Multi-User System Design
The system now supports:
.Donors → donate food
.Receivers → request food
.Donors/Admin → view requests
This makes the application closer to real production systems.

##Day 5 helped me understand how real-world systems handle multiple user roles and how backend routes are designed accordingly.