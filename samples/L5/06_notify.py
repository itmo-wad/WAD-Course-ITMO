#
# pip install requests
#
from flask import Flask, render_template, request
from werkzeug.exceptions import InternalServerError
import requests

users = {
    "user": "",
    "admin": "secretpass"
}


app = Flask(__name__)


@app.route('/')
def home():
    name = request.args.get("name")
    return f"Hello, {name}. Your password is: {users[name]}"
    
    
@app.errorhandler(InternalServerError)
def handle_500(e):
    # Docs: https://github.com/codex-bot/notify
    requests.post("https://notify.bot.codex.so/u/<...>", {
        "message": f"*Exception* on the server: `{str(e)}`",
        "parse_mode": "Markdown"
    })
    return str(e), 500
    

if __name__ == "__main__":
    # Debug should be False
    app.run(host='localhost', port=5000, debug=False)