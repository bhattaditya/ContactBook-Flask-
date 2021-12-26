from flask import Flask, render_template

app = Flask(__name__)

contacts = [
    {
        'name': 'Name of the contact',
        'phone': 'Number of the contact',
        'address': 'Address of the contact',
        'city': 'Location of the contact'
    }
]

@app.route("/")
def home():
    return render_template('home.html', contacts=contacts, title='ContactBook')

@app.route("/<anything>")
def some_random_text(anything):
    return render_template('anything.html', title='JustAnything')

@app.route("/about")
def about():
    return render_template('about.html', title='AboutPage')

if __name__ == "__main__":
    app.run(debug=True)

