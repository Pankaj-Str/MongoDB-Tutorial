# MongoDB Query API
MongoDB Query API allows you to interact with your MongoDB database to retrieve, update, and manipulate data. MongoDB supports a rich set of query operators that you can use to filter, project, and manipulate data within your collections. Here are some commonly used MongoDB Query API operations:

### Basic Query Operations:

1. **Find Documents:**
   - Retrieve documents from a collection that match a query.

    ```javascript
    db.collection.find({ key: value })
    ```

2. **Equality and Field Existence:**
   - Find documents where a specific field has a certain value or exists.

    ```javascript
    db.collection.find({ field: value })
    ```

3. **Inequality:**
   - Find documents where a specific field has a value not equal to a certain value.

    ```javascript
    db.collection.find({ field: { $ne: value } })
    ```

4. **Logical AND:**
   - Combine multiple conditions using logical AND.

    ```javascript
    db.collection.find({ $and: [{ condition1 }, { condition2 }] })
    ```

### Comparison Operators:

1. **Greater Than:**
   - Find documents where a specific field has a value greater than a certain value.

    ```javascript
    db.collection.find({ field: { $gt: value } })
    ```

2. **Less Than:**
   - Find documents where a specific field has a value less than a certain value.

    ```javascript
    db.collection.find({ field: { $lt: value } })
    ```

3. **Greater Than or Equal To:**
   - Find documents where a specific field has a value greater than or equal to a certain value.

    ```javascript
    db.collection.find({ field: { $gte: value } })
    ```

4. **Less Than or Equal To:**
   - Find documents where a specific field has a value less than or equal to a certain value.

    ```javascript
    db.collection.find({ field: { $lte: value } })
    ```

### Querying Arrays:

1. **Array Elements Match:**
   - Find documents where an array field contains at least one element that matches a specified condition.

    ```javascript
    db.collection.find({ arrayField: { $elemMatch: { condition } } })
    ```

2. **Array Size:**
   - Find documents where an array field has a specific size.

    ```javascript
    db.collection.find({ arrayField: { $size: size } })
    ```

### Projection:

1. **Select Fields to Return:**
   - Retrieve documents with only the specified fields.

    ```javascript
    db.collection.find({}, { field1: 1, field2: 1, _id: 0 })
    ```

### Update Operations:

1. **Update Documents:**
   - Update documents that match a specified condition.

    ```javascript
    db.collection.update({ condition }, { $set: { updateFields } })
    ```

2. **Update or Insert (Upsert):**
   - Update documents that match a specified condition or insert a new document if no match is found.

    ```javascript
    db.collection.update({ condition }, { $set: { updateFields } }, { upsert: true })
    ```

These are just a few examples of the MongoDB Query API operations. The MongoDB documentation is a valuable resource for exploring the full range of query operators and their usage: [MongoDB Query and Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/).
