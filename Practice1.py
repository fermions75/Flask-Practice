from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "this is flask page okay"

@app.route("/about")
def about_page():
    return "this is flask page about"


app.run(debug=True)
