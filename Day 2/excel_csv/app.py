from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import os
import uuid

app=Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
            return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file is None:
        return 'No file uploaded', 400

    # Try reading as Excel, if fails, try as CSV
    try:
        df = pd.read_excel(file)
    except Exception:
        file.seek(0)
        df = pd.read_csv(file, encoding='latin1', on_bad_lines='skip')

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    file_name = f"{uuid.uuid4()}.csv"
    file_path = os.path.join('downloads', file_name)
    df.to_csv(file_path, index=False)
    
    return render_template('download.html', file_path=file_path)

@app.route("/download/<file_path>", methods=["POST"])
def download(file_path): 
    directory, filename = os.path.split(file_path)
    return send_from_directory(directory, filename, as_attachment=True)
     
    
  




if __name__=="__main__":
    app.run(debug=True, port=5000)
