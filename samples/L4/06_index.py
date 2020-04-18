#
# pip3 install pymongo
#
import random
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.wad

# Add 5kk documents
for user in range(1000):
    db.users2.insert_many([{"username":random.randint(0,1000000), "password":random.randint(0,1000000)} for i in range(5000)])