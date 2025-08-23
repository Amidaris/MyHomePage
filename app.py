from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('aboutme'))

@app.route('/mypage/me', methods=['GET'])
def aboutme():
   if request.method == 'GET':
        return render_template("aboutme.html")


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
        return render_template("contact.html")
   elif request.method == 'POST':
    return '<h1>Wiadomość została prawidłowo przesłana.</h1>'