from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'the random string'


@app.route('/')
def hello():
    name = request.args.get("name", "")
    if name == "alex":
        flash(f"Goodbye, {name}", "success")
    else:
        flash(f"No such user: {name}", "danger")
    
    return redirect(url_for("poka"))
    
    
@app.route('/poka')
def poka():
    return render_template("goodbye.html")
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)