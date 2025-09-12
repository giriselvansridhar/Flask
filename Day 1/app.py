from flask import Flask 

app = Flask(__name__)


@app.route("/hello/<int:name>", methods=["GET"])
def home(name):
    return f"Hello, your number is {name}"


@app.route("/about")
def about():
    return "This is the about page."
    


if __name__=="__main__":
    app.run(debug=True, port=5000)