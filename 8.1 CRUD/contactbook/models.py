from contactbook import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    id (int): id will be unique
    username (str): name of the user
    email (str): email of the user
    password (str): password of the user

    conatcts : relationshp to Contact objects i.e User can have many Contacts
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contacts = db.relationship('Contact', backref='creator', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"


class Contact(db.Model):
    """
    id (int): id of the contact
    name (str): name of the contact
    phone (str): number of the contact
    city (str): city of the contact
    address (str): address of the contact

    user_id (int): foreign key to USER(user.id)
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self) -> str:
        return f"Contact('{self.name}', '{self.phone}', '{self.email}')"
