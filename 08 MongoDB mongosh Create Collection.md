# MongoDB mongosh Create Collection 

---

### **Step-by-Step Guide to Create a Collection**

#### **Step 1: Start MongoDB Shell**
1. Open your terminal or command prompt.
2. Start `mongosh` by typing:
   ```bash
   mongosh
   ```

#### **Step 2: Switch to the Database**
1. Use the `use <databaseName>` command to select or create a database.
   ```javascript
   use myDatabase
   ```
   - If the database doesn't exist, MongoDB will create it when you add data or explicitly create a collection.

#### **Step 3: Create a Collection**
1. Use the `createCollection` method to create a collection explicitly.
   ```javascript
   db.createCollection("myCollection");
   ```
   - Replace `"myCollection"` with your desired collection name.

#### **Step 4: Verify the Collection**
1. Use the `show collections` command to list all collections in the database.
   ```javascript
   show collections
   ```

---

### **Example**
Here’s a complete session in **mongosh**:

```javascript
// Step 1: Switch to a database
use myDatabase;

// Step 2: Create a collection named 'students'
db.createCollection("students");

// Step 3: Verify the collection
show collections;
```

---

### **Expected Output**
After running the above commands, you should see the following:

1. When creating the collection:
   ```text
   { ok: 1 }
   ```
2. When listing collections:
   ```text
   students
   ```

---

### **Important Notes**
- **Automatic Collection Creation:** If you insert a document into a non-existing collection, MongoDB will create the collection for you automatically.
- **Explicit Creation:** Use `createCollection` only if you need to configure options or want to ensure the collection exists before inserting data.

This simple process helps you explicitly create and manage collections in MongoDB!

