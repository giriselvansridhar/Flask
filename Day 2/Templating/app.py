from flask import Flask, request, Response, render_template
app=Flask(__name__, template_folder='templates')





@app.route("/other", methods=["GET"])
def other():
    return "This is other page" 


@app.route("/", methods=["GET"])
def home():


    Name="Giriselvan"
    age=20



    return render_template('index.html', Name=Name, age=age)


@app.add_template_filter
def reverse(s):
    return s[::-1]

if __name__=="__main__":
    app.run(debug=True, port=5000)