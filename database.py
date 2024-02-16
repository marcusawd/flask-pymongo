from pymongo import MongoClient

import os

client = MongoClient(os.getenv("MONGODB"))
db = client[os.getenv("DB_NAME")]
