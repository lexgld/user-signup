from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login_form.html', title="Signup")
def test_len(field):
    if len(field)>=3 and len(field)<=20:
        return True
    else:
        return False

def test_space(field):
    if ' ' not in field:
        return True
    else:
        return False
 
def validate_field(field):
    if not test_len(field) or not test_space(field):
        return False
    else:
        return True

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_match_error = ''
    email_error = ''

    if not validate_field(username):
        username_error = 'Chosen username is invalid. It must be between 3 and 20 characters long.' 

    if not validate_field(password):
        password_error = 'Chosen password is invalid. It must be between 3 and 20 characters long.'
    
    if password != verify_password:
        password_match_error = 'Passwords do not match.'

    if not username_error and not password_error and not password_match_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('login_form.html', username=username, email=email, username_error=username_error, password_error=password_error, password_match_error=password_match_error, email_error=email_error)

@app.route('/welcome')
def valid_login():
    username = request.args.get('username')
    return render_template('welcome.html', title="Welcome", username=username)

app.run()