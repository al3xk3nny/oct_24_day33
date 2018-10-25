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

coll = conn[DBS_NAME][COLLECTION_NAME] # conn[DBS_NAME] datatype is a dictionary and so is conn[DBS_NAME][COLLECTION_NAME]. In other words, if db = conn[DBS_NAME], then db[COLLECTION_NAME].

documents = coll.find()

for doc in documents:
    print(doc)