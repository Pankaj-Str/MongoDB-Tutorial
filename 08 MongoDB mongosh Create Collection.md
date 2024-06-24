# MongoDB mongosh Create Collection 

### Step-by-Step Guide: Creating a Collection Using `mongosh`

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

#### Step 3: Switch to a Database

First, switch to the database where you want to create the collection. If the database doesn't exist, it will be created when you switch to it. For example, to switch to a database named `codeswithpankaj`, type:

```sh
use codeswithpankaj
```

You should see a message indicating that you've switched to the new database:

```sh
switched to db codeswithpankaj
```

#### Step 4: Create a Collection

To create a collection, use the `db.createCollection` method. For example, to create a collection named `users`, type:

```sh
db.createCollection("users")
```

You should see a confirmation message like this:

```sh
{ ok: 1 }
```

#### Step 5: Verify the Collection Creation

To verify that the collection was created, you can list all collections in the database using the `show collections` command. Type:

```sh
show collections
```

You should see the `users` collection listed:

```sh
users
```

### Summary

Congratulations! You have successfully created a collection in MongoDB using `mongosh`.

In summary, the steps are:
1. Ensure the MongoDB server is running.
2. Open `mongosh`.
3. Use the `use` command to switch to the desired database.
4. Create a collection using `db.createCollection`.
5. Verify the collection creation using `show collections`.

