from flask import render_template, url_for, flash, redirect
from contactbook.models import User, Contact
from contactbook.form import RegistrationForm, LoginForm
from contactbook import app

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
