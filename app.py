from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key_here"

@app.route("/")
def home():
    return "Food Donation Platform is Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)
