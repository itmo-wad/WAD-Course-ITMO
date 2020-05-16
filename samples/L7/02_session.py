from flask import Flask, request, make_response
import hashlib
import hmac

app = Flask(__name__)

users = {
    "user": "user",
    "guest": "guest"
}

SECRET_KEY = b"randomSecretString"

@app.route('/cabinet/')
def cabinet():
    username = request.cookies.get('username')
    token = request.cookies.get('token')
    
    if not hmac.compare_digest(
        hmac.new(SECRET_KEY, username.encode(), hashlib.sha256).hexdigest(),
        token
    ):
       return "Forbidden" 
    
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


def decode_flask_cookie(secret_key, cookie_str):
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)


if __name__ == '__main__':

    name_to_sign = "guest"

    # Create valid hmac for the chosen name_to_sign if you know randomSecretString
    print(hmac.new(b"randomSecretString", name_to_sign.encode(), hashlib.sha256).hexdigest())

    # For standard Flask session, use decode_flask_cookie to decrypt cookie
    # Got from: https://gist.github.com/babldev/502364a3f7c9bafaa6db

    app.run()
