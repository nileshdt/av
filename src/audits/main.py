from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Get a reference to the "test" database
db = client["test"]

# Get a reference to the "customers" collection
customers_collection = db["customers"]

# Insert a new document into the "customers" collection
new_customer = {
    "name": "Tom1 Smith",
    "age": 30,
    "city": "New York"
}
customers_collection.insert_one(new_customer)

# Find all documents in the "customers" collection
customers = customers_collection.find()

# Print the name of each customer
for customer in customers:
    print(customer["name"])

# Update the age of the customer with name "John Smith"
customers_collection.update_one(
    {"name": "John Smith"},
    {"$set": {"age": 31}}
)

# Delete the customer with name "John Smith"
# customers_collection.delete_one({"name": "John Smith"})
