# MongoDB mongosh Create Collection 

In MongoDB, collections are created implicitly when you insert data into them. However, if you want to create an empty collection without inserting any data, you can use the `createCollection` method in the MongoDB shell (`mongosh`).

Here's how you can create an empty collection using `mongosh`:

1. **Open `mongosh` Shell:**
   - Open a terminal or command prompt.
   - Type `mongosh` and press Enter to start the MongoDB shell.

2. **Switch to a Database (Optional):**
   - If you want to work with a specific database, use the `use` command to switch to that database.

    ```javascript
    use mydatabase
    ```

   Replace "mydatabase" with the desired name of your database. If the database doesn't exist, MongoDB will create it when you insert data.

3. **Create an Empty Collection:**
   - Use the `createCollection` method to create an empty collection.

    ```javascript
    db.createCollection("myCollection")
    ```

   Replace "myCollection" with the desired name of your collection.

4. **Verify Collection Creation:**
   - You can check if the collection has been created by running the following command:

    ```javascript
    show collections
    ```

   This command will display a list of all collections in the current database, and you should see the one you just created.

Remember that in MongoDB, collections are created dynamically when you insert data into them. If you want to explicitly create an empty collection without inserting any documents, you can use the `createCollection` method as shown above.
