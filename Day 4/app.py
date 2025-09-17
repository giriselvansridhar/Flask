from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def home():
    return render_template('home.html', alt='A descriptive text for the image'  )



if __name__ == "__main__":
    app.run(debug=True)
