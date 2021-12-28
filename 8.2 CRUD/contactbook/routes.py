import time
from flask import render_template, url_for, flash, redirect, request
from contactbook.models import User, Contact
from contactbook.form import RegistrationForm, LoginForm, ContactForm
from contactbook import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
    if current_user.is_authenticated:
        contacts = Contact.query.filter_by(creator=current_user)
        if contacts.count() > 0:
            return render_template('home.html', contacts=contacts, title='ContactBook',new_heading = 'Listing Contacts')
        else:
            return render_template('home.html', title='ContactsBook',new_heading = 'No contacts')    
    return render_template('home.html', title='ContactBook',new_heading = 'Welcome to Contact Book... create your contacts easily')    

@app.route('/about')
def about():
    return render_template('about.html', title='AboutPage')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created {form.username.data}! Now you can login", 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Login  unsuccessfull. Please check email and password", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        time.sleep(2)
        return render_template('home.html', title='ContactBook',new_heading = 'You are successfully logged out!') 
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

# =====================================================================================================================================

# when contact is created redirect user to contacts_home file
@app.route('/contact/new', methods=['GET','POST'])
def new_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(name=form.name.data, email=form.email.data, phone=form.phone.data, city=form.city.data, address=form.address.data, creator=current_user)
        db.session.add(contact)
        db.session.commit()
        flash("Contact created!", 'success')
        return redirect(url_for('contacts_home'))
    return render_template('create_contact.html', title='New Contact', legend='New Contact', form = form)


@app.route('/contacts_home')
def contacts_home():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

# here testing
# ------------------------------------------------------------
# @app.route('/contact_id')
# def contact():
#     contact = Contact.query.get(8)
#     return render_template('contact.html', contact=contact)

# @app.route('/contact_id/<int:contact_id>')
# def contact(contact_id):
#     contact = Contact.query.get(contact_id)
#     return render_template('contact.html', contact=contact)

@app.route('/contact_id/<contact_id>')
def contact(contact_id):
    contact = Contact.query.get_or_404(int(contact_id))
    return render_template('contact.html', contact=contact)

@app.route('/contact_id/<contact_id>/update', methods=['GET','POST'])
@login_required
def update_contact(contact_id):
    contact = Contact.query.get_or_404(int(contact_id))
    form = ContactForm()  

    if form.validate_on_submit() :
         contact.name = form.name.data
         contact.email = form.email.data
         contact.phone = form.phone.data
         contact.city = form.city.data
         contact.address = form.address.data
         db.session.commit()
         flash('Contact Updated!', 'success')
         return redirect(url_for('contact', contact_id=int(contact.id)))

    elif request.method == 'GET':
        form.name.data = contact.name
        form.email.data = contact.email
        form.phone.data = contact.phone
        form.city.data = contact.city
        form.address.data = contact.address
    return render_template('create_contact.html', title='Update Contact', legend='Update Contact', form = form)


@app.route('/contact_id/<int:contact_id>/delete', methods=['POST'])
@login_required
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact Deleted!', 'success')
    return redirect(url_for('home'))


@app.route('/home/search_contact/<string:email>')
def search_contact(email):
    contacts = Contact.query.filter_by(email=email)
    if contacts.count() > 0:
        return render_template('home.html', contacts=contacts, title='Contacts',new_heading = 'Listing Contacts')
    else:
        return render_template('home.html',title='No contact', new_heading='No contact found searched email')


