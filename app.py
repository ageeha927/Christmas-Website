from markupsafe import escape
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/family')
def family():
    return render_template('family.html')

if __name__ == '__main__':
    app.run(debug=True)