from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route('/login')
def show_login_form():
    return render_template('login_form.template.html')

# if you recieve a POST request for the '/login' url
# use the function below
@app.route('/login', methods=["POST"])
def process_login_form():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print("data recieved")
    return "Welcome, " + username

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)