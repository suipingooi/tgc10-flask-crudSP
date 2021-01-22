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

@app.route('/calculate')
def show_calc_form():
    return render_template('calc_form.template.html')

@app.route('/calculate', methods=['POST'])
def process_calc_form():
    print(request.form)
    n1 = int(request.form.get('number1'))
    n2 = int(request.form.get('number2'))
    return str(n1 + n2)

@app.route('/bmi')
def show_bmi_form():
    return render_template('bmi.template.html')

@app.route('/bmi', methods=['POST'])
def process_bmi():
    print(request.form)
    h = float(request.form.get('height'))
    w = float(request.form.get('weight'))
    bmi = round(w/h**2, 2)
    return render_template('bmi_results.template.html', bmi=bmi)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)