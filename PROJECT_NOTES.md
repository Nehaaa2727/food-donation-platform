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
