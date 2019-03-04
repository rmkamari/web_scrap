import pymongo
import json

client = pymongo.MongoClient("148.251.102.221", 27017)
# Connection to the database
db = client.web_scrapping
# Collection
collection = db.source
i = 1
for obj in collection.find({}, {'_id': False}):
    print(obj['base_url'])
    for j in range(len(obj) - 1):
        print(obj['obj' + str(i)]['xpath'])
        print(obj['obj' + str(i)]['type'])
        print("-------------------------------------------")
        i += 1
