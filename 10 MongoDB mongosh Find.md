# MongoDB mongosh Find

In MongoDB, the `find` method is used to query and retrieve documents from a collection in **mongosh**. It allows you to specify filter criteria and project specific fields from the documents.

---

### **Syntax**
```javascript
db.collection.find(query, projection);
```

- **`query`**: A document specifying selection criteria (optional). If omitted, all documents in the collection are returned.
- **`projection`**: A document specifying which fields to include or exclude (optional).

---

### **Step-by-Step Guide to Use `find`**

#### **Step 1: Insert Sample Data**
Before using `find`, make sure the collection has some data.

```javascript
// Switch to a database
use myDatabase;

// Insert sample documents into the 'students' collection
db.students.insertMany([
    { name: "Alice", age: 22, grade: "A" },
    { name: "Bob", age: 25, grade: "B" },
    { name: "Charlie", age: 23, grade: "A" },
    { name: "Diana", age: 24, grade: "C" }
]);
```

---

#### **Step 2: Use `find` to Query Documents**

1. **Retrieve All Documents**
   ```javascript
   db.students.find();
   ```
   **Output:**
   ```json
   { "_id": ObjectId("..."), "name": "Alice", "age": 22, "grade": "A" }
   { "_id": ObjectId("..."), "name": "Bob", "age": 25, "grade": "B" }
   { "_id": ObjectId("..."), "name": "Charlie", "age": 23, "grade": "A" }
   { "_id": ObjectId("..."), "name": "Diana", "age": 24, "grade": "C" }
   ```

2. **Filter by a Specific Field**
   Retrieve all students with a grade of "A":
   ```javascript
   db.students.find({ grade: "A" });
   ```

3. **Retrieve Specific Fields**
   Retrieve only the `name` and `age` fields:
   ```javascript
   db.students.find({}, { name: 1, age: 1, _id: 0 });
   ```
   **Output:**
   ```json
   { "name": "Alice", "age": 22 }
   { "name": "Bob", "age": 25 }
   { "name": "Charlie", "age": 23 }
   { "name": "Diana", "age": 24 }
   ```

4. **Use Comparison Operators**
   Retrieve students older than 23:
   ```javascript
   db.students.find({ age: { $gt: 23 } });
   ```

5. **Combine Conditions**
   Retrieve students with grade "A" and age less than 23:
   ```javascript
   db.students.find({ grade: "A", age: { $lt: 23 } });
   ```

6. **Sort Results**
   Sort students by age in descending order:
   ```javascript
   db.students.find().sort({ age: -1 });
   ```

---

### **Common Query Operators**
- `$eq`: Equal to a value.
- `$ne`: Not equal to a value.
- `$gt`: Greater than a value.
- `$gte`: Greater than or equal to a value.
- `$lt`: Less than a value.
- `$lte`: Less than or equal to a value.
- `$in`: Matches any value in an array.
- `$or`: Combines multiple conditions with OR logic.
- `$and`: Combines multiple conditions with AND logic.

---

### **Advanced Example**
Retrieve students with either grade "A" or age greater than 23:
```javascript
db.students.find({
    $or: [
        { grade: "A" },
        { age: { $gt: 23 } }
    ]
});
```

---

### **Key Notes**
- The `find()` method returns a cursor, and in **mongosh**, it will automatically display the first 20 results.
- Use `.pretty()` to format the output for readability:
   ```javascript
   db.students.find().pretty();
   ```

This is how you use the `find` method to query documents in MongoDB effectively!
