from flask import Flask, render_template, request, Response
import pandas as pd

app=Flask(__name__, template_folder='templates')



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        # index.html should contain a form with username and password fields
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'giri' and password == 'password':
            return f'Welcome, {username}!'
        else:
            return 'Invalid credentials. Please try again.'

    
@app.route('/upload', methods=['POST'])
def upload():

    file=request.files.get('file')
    if file.content_type == "text/plain":
        return  file.read().decode('utf-8')
    else:
        df=pd.read_excel(file)
        return df.to_html()


@app.route("/csv", methods=["POST"])
def csv():
    file=request.files.get('file')
    df = pd.read_csv(file, encoding="latin1", delimiter=",", on_bad_lines='skip')
    response = Response(
        df.to_html(),
        status=200,
        mimetype='text/html',
        headers={
            "Content-Disposition": "attachment; filename=output.CSV"
        }
    )
    return response
if __name__=="__main__":
    app.run(debug=True, port=5000)
