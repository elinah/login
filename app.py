from flask import Flask, render_template, request

app = Flask(__name__)

info = ('username','password')
msg = ""

@app.route("/")
def form():
    return render_template('form.html', title = "Form")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #print request.form
    if (request.form['user'] == info[0] and request.form['pass'] == info[1]):
      msg = "Yay logged in successfully!"
    else:
      msg = "Incorrect username or password"
    return render_template('auth.html', title = "Authenticate", message = msg)

if __name__ == '__main__':
    app.debug = True
    app.run()
