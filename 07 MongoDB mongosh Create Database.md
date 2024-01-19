# MongoDB mongosh Create Database

1. **Open `mongosh` Shell:**
   - Open a terminal or command prompt.
   - Type `mongosh` and press Enter to start the MongoDB shell.

2. **Switch to a Database:**
   - Use the `use` command to switch to a specified database. If the database does not exist, MongoDB will create it when you insert the first document.

    ```javascript
    use mydatabase
    ```

   Replace "mydatabase" with the desired name of your database.

3. **Insert Data (Optional):**
   - To actually create the database, you need to insert data into a collection within that database. If the collection doesn't exist, MongoDB will create it when you insert the first document.

    ```javascript
    db.myCollection.insertOne({ key: value })
    ```

   Replace "myCollection" with the name of your collection.

4. **Verify Database Creation:**
   - You can check if the database has been created by running the following command:

    ```javascript
    show dbs
    ```

   This command will display a list of all databases, and you should see the one you created.

Remember, MongoDB is designed to be flexible with the creation of databases and collections. They are created implicitly when you insert data, and you don't need to explicitly create a database or collection before using it.
