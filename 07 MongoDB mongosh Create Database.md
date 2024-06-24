### Creating a MongoDB Database Using `mongosh`

#### Prerequisites

1. **MongoDB Server**: Ensure that MongoDB is installed and running on your machine. You can download MongoDB from the [MongoDB official website](https://www.mongodb.com/try/download/community).
2. **MongoDB Shell (`mongosh`)**: Ensure that `mongosh` is installed. You can download it from the [MongoDB Shell download page](https://www.mongodb.com/try/download/shell).

#### Step 1: Start the MongoDB Server

Make sure your MongoDB server is running. Open a terminal and start the MongoDB server by typing:

```sh
mongod
```

Leave this terminal window open as the MongoDB server needs to be running in the background.

#### Step 2: Open MongoDB Shell (`mongosh`)

Open a new terminal window and start the MongoDB Shell by typing:

```sh
mongosh
```

You will see output similar to this:

```sh
Current Mongosh Log ID: 60b6e0a...
Connecting to: mongodb://localhost:27017
MongoDB server version: 4.4.6
```

#### Step 3: Switch to a New Database

In MongoDB, you don't need to explicitly create a database. Simply switch to a new database using the `use` command. If the database doesn't exist, it will be created when you first insert data into it. For example, to create a database named `codeswithpankaj`, type:

```sh
use codeswithpankaj
```

You should see a message indicating that you've switched to the new database:

```sh
switched to db codeswithpankaj
```

#### Step 4: Create a Collection

In MongoDB, data is stored in collections. A collection is similar to a table in relational databases. To create a collection, use the `db.createCollection` method. For example, to create a collection named `users`, type:

```sh
db.createCollection("users")
```

You should see a confirmation message like this:

```sh
{ ok: 1 }
```

#### Step 5: Insert Documents into the Collection

Now that you have a collection, you can insert documents into it. To insert a document, use the `insertOne` method. For example, to insert a user document, type:

```sh
db.users.insertOne({ name: "Pankaj", age: 30, email: "pankaj@example.com" })
```

You should see a confirmation message like this:

```sh
{
  acknowledged: true,
  insertedId: ObjectId("60b6e0a...")
}
```

#### Step 6: Query the Collection

To verify that your document was inserted, you can query the collection using the `find` method. For example, to find all documents in the `users` collection, type:

```sh
db.users.find()
```

You should see the inserted document(s):

```sh
[
  { _id: ObjectId("60b6e0a..."), name: "Pankaj", age: 30, email: "pankaj@example.com" }
]
```

#### Step 7: Verify the Database Creation

To verify that your database has been created, you can list all databases using the `show dbs` command. Note that the database will not appear in the list until it contains data. Since we have already inserted a document, you should see `codeswithpankaj` in the list:

```sh
show dbs
```

You should see something like this:

```sh
admin         0.000GB
codeswithpankaj  0.001GB
config        0.000GB
local         0.000GB
```

### Summary

Congratulations! You have successfully created a MongoDB database named `codeswithpankaj` and added a collection with some data using `mongosh`.

In summary, the steps are:
1. Ensure MongoDB server is running.
2. Open `mongosh`.
3. Use the `use` command to create and switch to a new database.
4. Create a collection using `db.createCollection`.
5. Insert documents using `insertOne`.
6. Query the collection using `find`.
7. Verify the database creation using `show dbs`.

Feel free to add more collections and documents to your database as needed. Happy coding!
