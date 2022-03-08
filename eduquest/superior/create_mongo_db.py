from pprint import pprint

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db.test_collection
db.inventory.insert_one({'item': "canvas", 'qty': 100, 'tags': ["cotton"], 'size': {'h': 28, 'w': 35.5, 'uom': "cm"}})
t = db.inventory.find({})
pprint(list(t))
