from flask import Flask, request, make_response, abort
from functools import wraps
import hashlib
import hmac

app = Flask(__name__)

users = {
    "user": "user",
    "guest": "guest"
}

SECRET_KEY = b"randomSecretString"

def check_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = request.cookies.get('username')
        token = request.cookies.get('token')
        if not username or not token or not hmac.compare_digest(
            hmac.new(SECRET_KEY, username.encode(), hashlib.sha256).hexdigest(),
            token
        ):
            abort(403, description="Auth required")
        return f(*args, **kwargs)
    return decorated_function


@app.route('/cabinet/')
@check_auth
def cabinet():
    username = request.cookies.get('username')
    return f"Hello {username}"
    
    
@app.route('/cabinet2/')
def cabinet2():
    username = request.cookies.get('username')
    return f"Hello {username}"
    
    
@app.route('/auth/<username>')
def auth(username):
    password = request.args.get("password")
    
    if username not in users:
        return "Forbidden"
    if users[username] != password:
        return "Forbidden"
        
    token = hmac.new(SECRET_KEY, username.encode(), hashlib.sha256).hexdigest()
        
    resp = make_response(f"Hello {username}")
    resp.set_cookie('username', username)
    resp.set_cookie('token', token)
    return resp


if __name__ == '__main__':
    app.run()
