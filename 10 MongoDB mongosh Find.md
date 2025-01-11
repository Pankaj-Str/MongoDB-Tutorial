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

# How to use MongoDB's common query operators in **mongosh**:

---

### **Sample Data**
Let's use a collection named `products` with the following documents:

```javascript
use myDatabase;

db.products.insertMany([
    { name: "Laptop", price: 800, category: "Electronics", stock: 10 },
    { name: "Phone", price: 600, category: "Electronics", stock: 25 },
    { name: "Tablet", price: 300, category: "Electronics", stock: 15 },
    { name: "Chair", price: 100, category: "Furniture", stock: 50 },
    { name: "Desk", price: 200, category: "Furniture", stock: 20 },
    { name: "Lamp", price: 50, category: "Furniture", stock: 30 }
]);
```

---

### **Query Examples**

#### **1. `$eq`: Equal to a value**
Find all products in the "Electronics" category:
```javascript
db.products.find({ category: { $eq: "Electronics" } });
```

#### **2. `$ne`: Not equal to a value**
Find all products that are not in the "Furniture" category:
```javascript
db.products.find({ category: { $ne: "Furniture" } });
```

#### **3. `$gt`: Greater than a value**
Find all products with a price greater than 500:
```javascript
db.products.find({ price: { $gt: 500 } });
```

#### **4. `$gte`: Greater than or equal to a value**
Find all products with a price greater than or equal to 300:
```javascript
db.products.find({ price: { $gte: 300 } });
```

#### **5. `$lt`: Less than a value**
Find all products with stock less than 20:
```javascript
db.products.find({ stock: { $lt: 20 } });
```

#### **6. `$lte`: Less than or equal to a value**
Find all products with a price less than or equal to 100:
```javascript
db.products.find({ price: { $lte: 100 } });
```

#### **7. `$in`: Matches any value in an array**
Find all products in either the "Electronics" or "Furniture" category:
```javascript
db.products.find({ category: { $in: ["Electronics", "Furniture"] } });
```

#### **8. `$or`: Combines multiple conditions with OR logic**
Find all products with a price greater than 500 **OR** stock less than 20:
```javascript
db.products.find({
    $or: [
        { price: { $gt: 500 } },
        { stock: { $lt: 20 } }
    ]
});
```

#### **9. `$and`: Combines multiple conditions with AND logic**
Find all products in the "Electronics" category **AND** with a price less than 800:
```javascript
db.products.find({
    $and: [
        { category: "Electronics" },
        { price: { $lt: 800 } }
    ]
});
```

---

### **Result Examples**
**For `$or`:**
```json
{ "_id": ObjectId("..."), "name": "Laptop", "price": 800, "category": "Electronics", "stock": 10 }
{ "_id": ObjectId("..."), "name": "Tablet", "price": 300, "category": "Electronics", "stock": 15 }
{ "_id": ObjectId("..."), "name": "Chair", "price": 100, "category": "Furniture", "stock": 50 }
{ "_id": ObjectId("..."), "name": "Lamp", "price": 50, "category": "Furniture", "stock": 30 }
```

This demonstrates how to use these operators effectively in your queries.
