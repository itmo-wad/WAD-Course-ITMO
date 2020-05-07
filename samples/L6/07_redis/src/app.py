from flask import Flask, render_template, request, redirect
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://redis:6379/0'})

@app.route("/<int:num>")
@cache.cached(timeout=10)
def index(num):
    for i in range(2, num):
        if num % i == 0:
            return f"Found divisor: {i}"


@app.route("/test")
@cache.cached(timeout=10)
def test():
    for i in range(2, 196644893598169):
        if 196644893598169 % i == 0:
            return f"Found divisor: {i}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)