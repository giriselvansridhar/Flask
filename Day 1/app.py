from flask import Flask, request, Response
app = Flask(__name__)
@app.route("/hello/<int:name>", methods=["GET"])
def home(name):
    return f"Hello, your number is {name}"


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return Response("This is the about page.", status=200, mimetype='text/plain')
    elif request.method == "POST":
        return Response("POST method not allowed on this endpoint.", status=405)
    
    return "This is the about page."



if __name__=="__main__":
    app.run(debug=True, port=5000)