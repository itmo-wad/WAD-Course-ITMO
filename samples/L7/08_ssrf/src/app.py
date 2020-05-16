from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)



@app.route("/")
def index():
    return "<form action=/check method=GET><input type=text name=url></form>"

@app.route("/check")
def check():
    r = requests.get(request.args.get("url"))
    return f"Website status is: {r.status_code}. <br>Code is:<br>{r.text}"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)