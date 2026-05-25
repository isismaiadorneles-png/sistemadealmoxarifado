from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/selecionar.html')
def selecionar():
    return render_template("selecionar.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/estoque.html')
def estoque():
    return render_template("estoque.html")

@app.route('/solicitar.html')
def solicitar():
    return render_template("solicitar.html")

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)