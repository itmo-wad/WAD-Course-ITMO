#
# pip3 install pymongo
#
import random
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.wad

def create():
    db.users.insert_many([{"username": random.randint(0, 10), "password": random.randint(0, 10)} for _ in range(10000)])

def clear():
    db.users.drop()
    
def measure(f):
    t = time.time()
    f()
    print(f"Operation time of {f} = {time.time() - t}")


measure(create)

## It will drop the collection
measure(clear)


def find():
    print("First: ", db.users.find_one({"username": 3}))
    for user in db.users.find({"username": 3}):
        print(user)
    
    
find()