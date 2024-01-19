# MongoDB mongosh Delete

In MongoDB, you can use the `deleteOne` or `deleteMany` methods in the `mongosh` shell to remove documents from a collection based on specified criteria. Here's how you can use these methods:

### Delete a Single Document:

```javascript
// Switch to the desired database (optional)
use mydatabase

// Delete a single document from a collection
db.myCollection.deleteOne({ key: value })
```

Replace "mydatabase" with the name of your database and "myCollection" with the name of your collection. Adjust the filter criteria to match the document you want to delete.

### Delete Multiple Documents:

```javascript
// Delete multiple documents from a collection
db.myCollection.deleteMany({ key: value })
```

This is similar to `deleteOne`, but it deletes multiple documents that match the filter criteria.

### Delete All Documents in a Collection:

```javascript
// Delete all documents from a collection
db.myCollection.deleteMany({})
```

Be cautious when using this command, as it will remove all documents from the specified collection.

### Verify Deletion:

After performing a deletion, you can verify the changes by querying the collection:

```javascript
// Find remaining documents in the collection
db.myCollection.find({})
```

Remember to adjust the code snippets based on your specific use case and data model. Deleting documents is a powerful operation, so use it with care. Always ensure that you have a backup or are working with test data when performing delete operations.
