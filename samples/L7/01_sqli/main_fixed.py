import os, hashlib
from flask import Flask, jsonify, render_template, request, g
from peewee import *

app = Flask(__name__)
database = SqliteDatabase('sample.db')


class Employees(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = database
        table_name = 'employees'
        primary_key = False


class ShopItems(Model):
    name = CharField()
    quantitiy = IntegerField()
    price = IntegerField()

    class Meta:
        database = database
        table_name = 'shop_items'
        primary_key = False
        
        
@app.before_request
def before_request():
    database.connect()

@app.after_request
def after_request(response):
    database.close()
    return response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

#API routes
@app.route('/api/v1.0/storeLoginAPI/', methods=['POST'])
def loginAPI():
    if request.method == 'POST':
        uname, pword = (request.json['username'],request.json['password'])
        print(hash_pass(pword))
        try:
            Employees.get(
                (Employees.username==uname) & 
                (Employees.password==hash_pass(pword))
            )
            result = {'status': 'success'}
        except DoesNotExist:
            result = {'status': 'fail'}
       
        return jsonify(result)

@app.route('/api/v1.0/storeAPI/<item>', methods=['GET'])
def searchAPI(item):
    results = []
    for item in ShopItems.select().where(ShopItems.name == item):
        results.append({
            "name": item.name,
            "quantity": item.quantitiy,
            "price": item.price
        })
    return jsonify(results)


@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('error.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error)


def hash_pass(passw):
	m = hashlib.md5()
	m.update(passw.encode('utf-8'))
	return m.hexdigest()

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
