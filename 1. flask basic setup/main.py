from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Contact Book</h1>"

@app.route("/<anything>")
def some_random_text(anything):
    return f"<h1>OOPS!!! -> {anything}</h1>"

@app.route("/about")
def about():
    return "<h1>Contact can be added, modifed or deleted.</h1>"

if __name__ == "__main__":
    app.run(debug=True)

