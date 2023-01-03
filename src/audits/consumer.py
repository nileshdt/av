import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection

audit = {
    "type": "audit",
    "description": "audit record",
    "data": "data",
    "createdBy": "createdBy",
    "createdOn": datetime.datetime.utcnow(),
    "modifiedBy": "modifiedBy",
    "modifiedOn": datetime.datetime.utcnow()}

audits = db.audithistory
post_id = audits.insert_one(audit).inserted_id
print(post_id)

print(db.collection_names(include_system_collections=False))

for audit in audits.find():
    print(audit)
