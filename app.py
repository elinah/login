from flask import Flask, render_template, request, session, redirect, url_for
from utils import formInput
import hashlib

app = Flask(__name__)
app.secret_key = '\xa2\xc7\x80h7yM\x0f\x88\xa4/c\x99\xd1\xc2\x9fh\xc5\xa1\xc1\xc5!\xde&O\r\xf9[\x97*\xd2i'

@app.route("/")
@app.route("/login/")
def form():
    if 'username' in session:
      return render_template('successfulLogin.html', title = "Logged In", username = session['username'])
    return render_template('form.html', title = "Form")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    msg = formInput.login(hashlib.sha256(request.form['user']).hexdigest(), 
        hashlib.sha256(request.form['pass']).hexdigest())
    if msg == "Yay you successfully logged in!":
        session['username'] = request.form['user']
    return render_template('auth.html', title = "Authenticate", message = msg)
        
@app.route("/register/", methods = ['POST'])
def reg():
    return render_template('auth.html', title = "Register", 
      message = formInput.register(hashlib.sha256(request.form['user']).hexdigest(), 
        hashlib.sha256(request.form['pass']).hexdigest()))
        
@app.route("/logout/", methods = ['POST'])
def logout():
    session.pop('username',None)
    return redirect(url_for('form'))
    

if __name__ == '__main__':
    app.debug = True
    app.run()
