#
# pip3 install pymongo
#
import random
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.wad

def create_01():
    for i in range(1000):
        username = random.randint(0, 10)
        password = random.randint(0, 100)
        db.users.insert({
            "username": username,
            "password": password
        })
    
def create_02():
    users = []
    for i in range(1000):
        username = random.randint(0, 10)
        password = random.randint(0, 100)
        users.append({"username": username, "password": password})

    db.users.insert_many(users)
    
    
t = time.time()

create_01()
create_02()

print(f"Operation time = {time.time() - t}")