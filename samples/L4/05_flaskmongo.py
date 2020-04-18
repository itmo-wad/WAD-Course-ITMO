from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    online_users = mongo.db.users.find({})
    return render_template("list.html", users=online_users)
        
        
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
