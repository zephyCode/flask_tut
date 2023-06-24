from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feebacks.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)

class Feedbacks(db.Model):
    ID = db.Column("User_ID", db.INTEGER, primary_key=True)
    name = db.Column("Name", db.String(100))
    message = db.Column("Message", db.String(1500))

    def __init__(self, name, message):
        self.name = name
        self.message = message

db.create_all()

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        feedbacks = Feedbacks(name, message)
        db.session.add(feedbacks)
        db.session.commit()
    return render_template('index.html')

@app.route('/tushar')
def tushar():
    return render_template('tushar.html')

@app.route('/yash')
def yash():
    return render_template('/yash.html')

if __name__ == "__main__":
    app.run(debug=True)