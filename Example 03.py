from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Access a specific database
db = client['my_database']

# Access a specific collection within the database
users_collection = db['users']

# Define a list of users
users = [
    {
        'name': 'Rahul Sharma',
        'age': 28,
        'email': 'rahul@p4n.in'
    },
    {
        'name': 'Neha Patel',
        'age': 30,
        'email': 'neha@p4n.in'
    },
    {
        'name': 'Amit Singh',
        'age': 35,
        'email': 'amit@p4n.in'
    }
]

# Insert multiple users into the collection
result = users_collection.insert_many(users)
print("Users inserted successfully:", result.inserted_ids)

# Find all users in the collection
all_users = users_collection.find()
print("All users:")
for user in all_users:
    print(user)

# Close the connection to the MongoDB server
client.close()