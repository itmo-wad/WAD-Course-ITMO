from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap
import os
from werkzeug.utils import secure_filename
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
import logging


app = Flask(__name__)
Bootstrap(app)

handler = logging.handlers.RotatingFileHandler('logs/app.log', maxBytes=320*1024, backupCount=2)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s [in %(pathname)s:%(lineno)d]: %(message)s '))

app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)
app.logger.info('This message goes to stderr and app.log!')


@app.route('/', methods=['GET', 'POST'])
def hello():
    name = request.args.get("name", "")
    app.logger.info(f"User with name {name}")
    
    return render_template("hello.html", name=name)
    
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)