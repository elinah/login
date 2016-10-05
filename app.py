from flask import Flask, render_template, request
from utils import formInput
import hashlib

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html', title = "Form")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    return render_template('auth.html', title = "Authenticate", 
      message = formInput.login(hashlib.sha256(request.form['user']).hexdigest(), 
        hashlib.sha256(request.form['pass']).hexdigest()))
        
@app.route("/register/", methods = ['POST'])
def reg():
    return render_template('auth.html', title = "Register", 
      message = formInput.register(hashlib.sha256(request.form['user']).hexdigest(), 
        hashlib.sha256(request.form['pass']).hexdigest()))

if __name__ == '__main__':
    app.debug = True
    app.run()
