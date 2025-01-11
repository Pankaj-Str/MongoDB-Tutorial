# MongoDB mongosh Update

---

### **Update Methods**
1. **`updateOne()`**: Updates the first document that matches the filter.
2. **`updateMany()`**: Updates all documents that match the filter.
3. **`replaceOne()`**: Replaces an entire document with a new one.

---

### **Syntax**

#### **`updateOne`**
```javascript
db.collection.updateOne(filter, update, options);
```

#### **`updateMany`**
```javascript
db.collection.updateMany(filter, update, options);
```

#### **`replaceOne`**
```javascript
db.collection.replaceOne(filter, replacement, options);
```

- **`filter`**: Specifies the criteria to match documents.
- **`update`**: Specifies the update operations to apply.
- **`replacement`**: A new document to replace the existing one (for `replaceOne`).
- **`options`**: Optional parameters (e.g., `upsert` to insert a new document if no match is found).

---

### **Example: Update in MongoDB**

#### **Sample Data**
```javascript
db.products.insertMany([
    { name: "Laptop", price: 800, category: "Electronics", stock: 10 },
    { name: "Phone", price: 600, category: "Electronics", stock: 25 },
    { name: "Chair", price: 100, category: "Furniture", stock: 50 }
]);
```

---

#### **1. Update a Single Document (`updateOne`)**
Increase the stock of the "Laptop" by 5:
```javascript
db.products.updateOne(
    { name: "Laptop" }, // Filter
    { $inc: { stock: 5 } } // Update operation
);
```

**Result:**
```json
{ "acknowledged": true, "matchedCount": 1, "modifiedCount": 1 }
```

---

#### **2. Update Multiple Documents (`updateMany`)**
Change the category of all products with a price greater than 500 to "Premium Electronics":
```javascript
db.products.updateMany(
    { price: { $gt: 500 } }, // Filter
    { $set: { category: "Premium Electronics" } } // Update operation
);
```

**Result:**
```json
{ "acknowledged": true, "matchedCount": 2, "modifiedCount": 2 }
```

---

#### **3. Replace a Document (`replaceOne`)**
Replace the document for "Chair" with a new one:
```javascript
db.products.replaceOne(
    { name: "Chair" }, // Filter
    { name: "Armchair", price: 150, category: "Furniture", stock: 30 } // Replacement document
);
```

**Result:**
```json
{ "acknowledged": true, "matchedCount": 1, "modifiedCount": 1 }
```

---

#### **4. Upsert Option**
If no document matches, insert a new document:
```javascript
db.products.updateOne(
    { name: "Tablet" }, // Filter
    { $set: { price: 300, category: "Electronics", stock: 15 } }, // Update operation
    { upsert: true } // Option
);
```

**Result:**
If the document doesn't exist, it will be created.

---

#### **5. Update with Multiple Operations**
Perform multiple updates in a single operation:
```javascript
db.products.updateOne(
    { name: "Laptop" },
    {
        $set: { price: 850 }, // Set a new price
        $inc: { stock: 2 } // Increase stock by 2
    }
);
```

---

### **Common Update Operators**
- `$set`: Set the value of a field.
- `$unset`: Remove a field.
- `$inc`: Increment a field by a value.
- `$mul`: Multiply a field by a value.
- `$rename`: Rename a field.
- `$min`: Update a field only if the new value is less than the current value.
- `$max`: Update a field only if the new value is greater than the current value.

---

### **Verify the Updates**
You can check the updated documents using:
```javascript
db.products.find().pretty();
```

# Common update operators** using the `updateOne` and `updateMany` methods in **mongosh**.

---

### **Sample Data**
Insert the following sample data into a collection named `employees`:
```javascript
db.employees.insertMany([
    { name: "Alice", age: 25, salary: 5000, department: "HR" },
    { name: "Bob", age: 30, salary: 6000, department: "Engineering" },
    { name: "Charlie", age: 35, salary: 7000, department: "Sales" }
]);
```

---

### **Examples**

#### **1. `$set`: Set the value of a field**
Update Bob's department to "Product Management":
```javascript
db.employees.updateOne(
    { name: "Bob" }, // Filter
    { $set: { department: "Product Management" } } // Update operation
);
```

---

#### **2. `$unset`: Remove a field**
Remove the `age` field from Alice's document:
```javascript
db.employees.updateOne(
    { name: "Alice" }, // Filter
    { $unset: { age: "" } } // Update operation
);
```

---

#### **3. `$inc`: Increment a field by a value**
Increase Charlie's salary by 1000:
```javascript
db.employees.updateOne(
    { name: "Charlie" }, // Filter
    { $inc: { salary: 1000 } } // Update operation
);
```

---

#### **4. `$mul`: Multiply a field by a value**
Double Bob's salary:
```javascript
db.employees.updateOne(
    { name: "Bob" }, // Filter
    { $mul: { salary: 2 } } // Update operation
);
```

---

#### **5. `$rename`: Rename a field**
Rename the `department` field to `team` for all employees:
```javascript
db.employees.updateMany(
    {}, // Filter (all documents)
    { $rename: { department: "team" } } // Update operation
);
```

---

#### **6. `$min`: Update a field only if the new value is less than the current value**
Set Alice's salary to 4500, but only if it's less than the current value:
```javascript
db.employees.updateOne(
    { name: "Alice" }, // Filter
    { $min: { salary: 4500 } } // Update operation
);
```

---

#### **7. `$max`: Update a field only if the new value is greater than the current value**
Set Charlie's salary to 8000, but only if it's greater than the current value:
```javascript
db.employees.updateOne(
    { name: "Charlie" }, // Filter
    { $max: { salary: 8000 } } // Update operation
);
```

---

### **Verify the Updates**
After running the above commands, you can view the updated documents:
```javascript
db.employees.find().pretty();
```

---

### **Expected Results**

**Before Updates:**
```json
{ "_id": ..., "name": "Alice", "age": 25, "salary": 5000, "department": "HR" }
{ "_id": ..., "name": "Bob", "age": 30, "salary": 6000, "department": "Engineering" }
{ "_id": ..., "name": "Charlie", "age": 35, "salary": 7000, "department": "Sales" }
```

**After Updates:**
```json
{ "_id": ..., "name": "Alice", "salary": 4500, "team": "HR" }
{ "_id": ..., "name": "Bob", "salary": 12000, "team": "Product Management" }
{ "_id": ..., "name": "Charlie", "salary": 8000, "team": "Sales" }
```

