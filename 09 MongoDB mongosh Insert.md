# MongoDB mongosh Insert 

In MongoDB, you can insert documents into a collection using the `insertOne` or `insertMany` methods. Here's how you can use these methods in the `mongosh` shell:

### Insert a Single Document:

```javascript
// Switch to the desired database (optional)
use mydatabase

// Insert a single document into a collection
db.myCollection.insertOne({
  key1: value1,
  key2: value2,
  // ... additional fields
})
```

Replace "mydatabase" with the name of your database and "myCollection" with the name of your collection. Adjust the document structure and key-value pairs according to your data.

### Insert Multiple Documents:

```javascript
// Switch to the desired database (optional)
use mydatabase

// Insert multiple documents into a collection
db.myCollection.insertMany([
  {
    key1: value1,
    key2: value2,
    // ... additional fields for document 1
  },
  {
    key1: value3,
    key2: value4,
    // ... additional fields for document 2
  },
  // ... additional documents
])
```

Again, replace "mydatabase" with the name of your database and "myCollection" with the name of your collection. Adjust the document structures and key-value pairs according to your data.

### Verify Insertion:

After inserting documents, you can verify the insertion by querying the collection:

```javascript
// Find all documents in the collection
db.myCollection.find()
```

This will display all documents in the specified collection.

Remember that collections and databases are created dynamically in MongoDB. If the specified collection or database doesn't exist, MongoDB will create them when you insert the first document.

Adjust the code snippets based on your specific use case and data model.
