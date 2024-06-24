### Step-by-Step Tutorial: Creating a MongoDB Database Using `mongosh`

#### Step 1: Install MongoDB

Before you can use `mongosh` (MongoDB Shell), ensure you have MongoDB installed on your machine. You can download and install it from the [MongoDB official website](https://www.mongodb.com/try/download/community).

#### Step 2: Install MongoDB Shell (`mongosh`)

MongoDB Shell (`mongosh`) is the new shell that comes with MongoDB. You can download and install `mongosh` from the [MongoDB Shell download page](https://www.mongodb.com/try/download/shell).

#### Step 3: Start MongoDB

Make sure your MongoDB server is running. You can start it by executing the following command in your terminal:

```sh
mongod
```

#### Step 4: Open MongoDB Shell (`mongosh`)

Once your MongoDB server is running, open a new terminal window and start the MongoDB Shell by typing:

```sh
mongosh
```

This will open the MongoDB Shell, and you'll see a prompt like this:

```sh
Current Mongosh Log ID: 60b6e0a...
Connecting to: mongodb://localhost:27017
MongoDB server version: 4.4.6
```

#### Step 5: Create a New Database

In MongoDB, databases are created dynamically. You don't need to explicitly create a database. Instead, you can simply switch to a new database, and it will be created when you insert data into it. To switch to a new database, use the `use` command followed by the database name. For example, to create a database named `codeswithpankaj`, you would type:

```sh
use codeswithpankaj
```

You should see a confirmation message like this:

```sh
switched to db codeswithpankaj
```

#### Step 6: Create a Collection

In MongoDB, data is stored in collections. A collection is similar to a table in relational databases. To create a collection, you can use the `db.createCollection` method. For example, to create a collection named `users`, type:

```sh
db.createCollection("users")
```

You should see a confirmation message like this:

```sh
{ ok: 1 }
```

#### Step 7: Insert Documents into the Collection

Now that you have a collection, you can insert documents (records) into it. To insert a document, use the `insertOne` method. For example, to insert a user document, type:

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

#### Step 8: Query the Collection

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

#### Step 9: Verify the Database Creation

To verify that your database has been created, you can list all databases using the `show dbs` command. However, note that the database will not appear in the list until it contains data. Since we have already inserted a document, you should see `codeswithpankaj` in the list:

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

#### Summary

Congratulations! You have successfully created a MongoDB database named `codeswithpankaj` and added a collection with some data using `mongosh`.

In summary, the steps are:
1. Install MongoDB and `mongosh`.
2. Start the MongoDB server.
3. Open `mongosh`.
4. Use the `use` command to create and switch to a new database.
5. Create a collection using `db.createCollection`.
6. Insert documents using `insertOne`.
7. Query the collection using `find`.
8. Verify the database creation using `show dbs`.

