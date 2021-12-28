from contactbook import db

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
