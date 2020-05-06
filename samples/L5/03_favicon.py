from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory("static", "favicon.ico", mimetype="image/vnd.microsoft.icon")


@app.route('/')
def index():
    return "Hello!"
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)