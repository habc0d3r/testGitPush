import pymongo

client = pymongo.MongoClient("mongodb+srv://hengulakash:hab.mongodb@cluster0.dtvgffq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "hengul",
    "email": "hengul@ineuron.ai",
    "surname": "akash"
}
d1 = {
    "name": "akash",
    "email": "akash@ineuron.ai",
    "surname": "boruah"
}
d2 = {
    "name": "boruah",
    "email": "boruah@ineuron.ai",
    "surname": "hengul"
}

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)
