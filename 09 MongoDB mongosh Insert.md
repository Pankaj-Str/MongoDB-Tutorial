# MongoDB mongosh Insert 

Inserting documents into a MongoDB collection using `mongosh` (MongoDB Shell) is a straightforward process. Here's a step-by-step guide to help you insert documents into a collection.

### Step-by-Step Guide: Inserting Documents Using `mongosh`

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

#### Step 3: Switch to the Database

Switch to the database where you want to insert documents. If the database doesn't exist, it will be created when you switch to it. For example, to switch to a database named `codeswithpankaj`, type:

```sh
use codeswithpankaj
```

You should see a message indicating that you've switched to the new database:

```sh
switched to db codeswithpankaj
```

#### Step 4: Insert a Single Document

To insert a single document into a collection, use the `insertOne` method. If the collection doesn't exist, it will be created when you insert the document. For example, to insert a document into a collection named `users`, type:

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

#### Step 5: Insert Multiple Documents

To insert multiple documents into a collection, use the `insertMany` method. For example, to insert multiple documents into the `users` collection, type:

```sh
db.users.insertMany([
  { name: "John", age: 25, email: "john@example.com" },
  { name: "Jane", age: 28, email: "jane@example.com" }
])
```

You should see a confirmation message like this:

```sh
{
  acknowledged: true,
  insertedIds: [
    ObjectId("60b6e0a..."),
    ObjectId("60b6e0b...")
  ]
}
```

#### Step 6: Verify the Insertions

To verify that your documents were inserted, you can query the collection using the `find` method. For example, to find all documents in the `users` collection, type:

```sh
db.users.find().pretty()
```

You should see the inserted documents:

```sh
[
  { _id: ObjectId("60b6e0a..."), name: "Pankaj", age: 30, email: "pankaj@example.com" },
  { _id: ObjectId("60b6e0b..."), name: "John", age: 25, email: "john@example.com" },
  { _id: ObjectId("60b6e0c..."), name: "Jane", age: 28, email: "jane@example.com" }
]
```

### Summary

Congratulations! You have successfully inserted documents into a MongoDB collection using `mongosh`.

In summary, the steps are:
1. Ensure the MongoDB server is running.
2. Open `mongosh`.
3. Use the `use` command to switch to the desired database.
4. Insert a single document using `insertOne`.
5. Insert multiple documents using `insertMany`.
6. Verify the insertions using `find`.

