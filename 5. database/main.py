from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '882b477e9403421a0aef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    contacts = db.relationship('Contact', backref='creator', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self) -> str:
        return f"Contact('{self.name}', '{self.phone}', '{self.email}')"


contacts = [
    {
        'name': 'Name of the contact',
        'phone': 'Number of the contact',
        'address': 'Address of the contact',
        'city': 'Location of the contact'
    }
]

@app.route('/')
def home():
    return render_template('home.html', contacts=contacts, title='ContactBook')

@app.route('/about')
def about():
    return render_template('about.html', title='AboutPage')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@book.com" and form.password.data == "book":
            flash(f"You are Logged In", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)

