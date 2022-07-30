import pymongo

client = pymongo.MongoClient("mongodb+srv://hengulakash:hab.mongodb@cluster0.dtvgffq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "hengul",
    "email": "hengul@ineuron.ai",
    "surname": "akash"
}

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)
