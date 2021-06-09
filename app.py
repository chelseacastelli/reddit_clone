
from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from helper_functions import salt_password
from flask_bcrypt import Bcrypt

# Variable to grab main application file
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://be8d953f0b3211:0ab47492@us-cdbr-east-04.cleardb.com/heroku_49586dd45308328'

# Database connection
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        _username = request.form['username']
        _email = request.form['email']
        _password = request.form['password']

        salted_pass = salt_password(_password)
        hashed_pass = bcrypt.generate_password_hash(salted_pass)

        try:
            new_user = User(username=_username, 
                            email=_email, 
                            password=hashed_pass)
            db.session.add(new_user)
            db.session.commit()
        except:
            print("There was an error creating your account.")
            return redirect('/')

        return redirect('/')

    return render_template('auth/reg.html')

if __name__ == '__main__':
    app.run(debug=True)

