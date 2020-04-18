from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import random
client = MongoClient('localhost', 27017)
db = client.wad
app = Flask(__name__)


@app.route("/")
def index():
    users = db.users.find({})
    return render_template("list.html", users=users)
    
    
@app.route("/age/<int:age>")
def age(age):
    users = db.users.find({"age": age})
    return render_template("list.html", users=users)
    


if __name__ == "__main__":
    db.users.drop()
    from faker import Faker
    faker = Faker()

    # Will insert new users each time
    db.users.insert_many([{"username": faker.name(), "age": random.randint(10, 25)} for _ in range(10)])
    app.run(host='localhost', port=5000, debug=True)