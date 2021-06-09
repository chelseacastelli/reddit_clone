
from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Variable to grab main application file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://be8d953f0b3211:0ab47492@us-cdbr-east-04.cleardb.com/heroku_49586dd45308328'

# Database connection
db = SQLAlchemy(app)


# Set up user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Allow up to 100 chars, don't allow it to be blank, & must be unique (not the same as someone else)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

