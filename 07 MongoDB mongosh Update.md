# MongoDB mongosh Update

In MongoDB, you can use the `updateOne` or `updateMany` methods in the `mongosh` shell to update documents in a collection based on specified criteria. Here's how you can use these methods:

### Update a Single Document:

```javascript
// Switch to the desired database (optional)
use mydatabase

// Update a single document in a collection
db.myCollection.updateOne(
  { key: value },   // Filter criteria
  { $set: { newKey: newValue } }  // Update operation
)
```

Replace "mydatabase" with the name of your database and "myCollection" with the name of your collection. Adjust the filter criteria to match the document you want to update, and specify the fields and values you want to update using the `$set` operator.

### Update Multiple Documents:

```javascript
// Update multiple documents in a collection
db.myCollection.updateMany(
  { key: value },   // Filter criteria
  { $set: { newKey: newValue } }  // Update operation
)
```

This is similar to `updateOne`, but it updates multiple documents that match the filter criteria.

### Upsert - Update or Insert:

If you want to update a document if it exists, and insert it if it doesn't exist, you can use the `upsert` option:

```javascript
// Update or insert a document in a collection (upsert)
db.myCollection.updateOne(
  { key: value },   // Filter criteria
  { $set: { newKey: newValue } },  // Update operation
  { upsert: true }  // Upsert option
)
```

### Verify Update:

After performing an update, you can verify the changes by querying the collection:

```javascript
// Find the updated document(s)
db.myCollection.find({ key: value })
```

Remember to adjust the code snippets based on your specific use case and data model. The `$set` operator is commonly used for field updates, but MongoDB provides various update operators for different update scenarios. Refer to the [MongoDB Update Operators documentation](https://docs.mongodb.com/manual/reference/operator/update/) for more details on update operations.
