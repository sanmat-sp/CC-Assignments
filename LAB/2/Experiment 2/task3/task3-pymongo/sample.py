from pymongo import MongoClient

#host = MongoClient("192.168.141.176")
host = MongoClient("mongodb")

db = host["sample_db"]
collection = db["sample_collection"]

sample_data = {"Name:":"<Sanmat>","SRN":"<PES1UG20CS385>"}
collection.insert_one(sample_data)
print('Inserted into the MongoDB database!')

rec_data = collection.find_one({"SRN":"<PES1UG20CS385>"})
print("Fecthed from MongoDB: ",rec_data)