import pymongo
import os

MONGODB_URI = os.environ.get("MONGODB_URI") # See bashrc file.
DBS_NAME = os.environ.get("DB_NAME") # See bashrc file.

COLLECTION_NAME = "people"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

doc = {
    "name": "alan",
    "age": 56,
    "hair": "red"
}

coll.insert(doc)