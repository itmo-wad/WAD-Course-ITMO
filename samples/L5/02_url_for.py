from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return f"<a href='{ url_for('index') }'>Home</a> | \
    <a href='{ url_for('login') }'>Login</a> | \
    <a href='{ url_for('register') }'>Register</a> | \
    <a href='{ url_for('profile', username='Alexander') }'>Profile</a>"

@app.route('/login')
def login():
    return 'login'
    
@app.route('/register/')
def register():
    return 'register'

@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile"

    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)