# MongoDB Using Key Commands


**Prerequisites:**
- Install MongoDB and `mongosh` (MongoDB Shell) as covered in previous modules.
- Open `mongosh` in your terminal/command prompt.
- All commands are run inside `mongosh`.

We'll cover:
1. Database Commands
2. Collection Commands
3. Insert Commands
4. Query & Read Commands
5. Update Commands
6. Delete Commands

Each step includes:
- The command.
- What it does.
- Example output (approximate, as `_id` values are unique).
- Verification tips.

Let's start!

## Step 1: Database Commands – Creating and Managing Databases
We'll create a database called "school".

1. **Switch to or Create Database**:
   - Command: `use school`
   - Description: Switches to the "school" database or creates it if it doesn't exist.
   - Run it:
     ```
     use school
     ```
   - Expected Output: `switched to db school`

2. **Show Current Database**:
   - Command: `db`
   - Description: Displays the name of the current database.
   - Run it:
     ```
     db
     ```
   - Expected Output: `school`

3. **List All Databases**:
   - Command: `show dbs` (or `show databases`)
   - Description: Lists all databases. Note: New databases won't show until data is added.
   - Run it:
     ```
     show dbs
     ```
   - Expected Output (initially may not show "school" if empty): 
     ```
     admin   0.000GB
     config  0.000GB
     local   0.000GB
     ```
     - We'll add data soon to make it visible.

4. **Database Stats**:
   - Command: `db.stats()`
   - Description: Shows stats like size and collections (empty now).
   - Run it:
     ```
     db.stats()
     ```
   - Expected Output (simplified):
     ```
     {
       "db": "school",
       "collections": 0,
       "objects": 0,
       "dataSize": 0,
       ...
     }
     ```

5. **Explicitly Create a Collection (to make DB visible)**:
   - Command: `db.createCollection("students")`
   - Description: Creates a collection explicitly.
   - Run it:
     ```
     db.createCollection("students")
     ```
   - Expected Output: `{ "ok" : 1 }`

Now, re-run `show dbs` – "school" should appear!

**Tip for Beginners:** Databases are lightweight; they only "exist" after data is added.

## Step 2: Collection Commands – Managing Collections
Collections are like tables. We'll work with "students".

1. **List Collections**:
   - Command: `show collections` (or `db.getCollectionNames()`)
   - Description: Lists collections in the current DB.
   - Run it:
     ```
     show collections
     ```
   - Expected Output: `students`

2. **Get Collection Reference**:
   - Command: `db.getCollection("students")`
   - Description: Returns a reference to the collection (useful for scripting).
   - Run it:
     ```
     db.getCollection("students")
     ```
   - Expected Output: `school.students` (just shows the name).

3. **Collection Stats**:
   - Command: `db.students.stats()`
   - Description: Shows detailed stats (empty now).
   - Run it:
     ```
     db.students.stats()
     ```
   - Expected Output (simplified):
     ```
     {
       "ns": "school.students",
       "size": 0,
       "count": 0,
       ...
     }
     ```

4. **Storage and Size Commands**:
   - Command: `db.students.storageSize()`
   - Description: Storage size in bytes.
   - Run it: Outputs a small number like `4096` (initial allocation).
   
   - Command: `db.students.totalSize()`
   - Description: Total size (data + indexes).
   - Run it: Similar to above.

   - Command: `db.students.dataSize()`
   - Description: Data size only.
   - Run it: `0` now.

5. **Count Documents**:
   - Command: `db.students.countDocuments({})`
   - Description: Accurate count of documents (0 now).
   - Run it:
     ```
     db.students.countDocuments({})
     ```
   - Expected Output: `0`

   - Alternative: `db.students.estimatedDocumentCount()` (faster for large collections).

**Tip for Beginners:** Avoid the deprecated `db.students.find().count()`.

6. **Rename Collection**:
   - Command: `db.students.renameCollection("pupils")`
   - Description: Renames "students" to "pupils".
   - Run it:
     ```
     db.students.renameCollection("pupils")
     ```
   - Expected Output: `{ "ok" : 1 }`
   - Now rename back: `db.pupils.renameCollection("students")`

7. **Create Capped Collection** (Optional Advanced):
   - Command: `db.createCollection("logs", { capped: true, size: 100000 })`
   - Description: Creates a fixed-size collection (good for logs).
   - Run it, then drop it later if not needed.

## Step 3: Insert Commands – Adding Data
Let's add student documents.

1. **Insert One Document**:
   - Command: `db.students.insertOne({ doc })`
   - Description: Inserts a single JSON-like document.
   - Example:
     ```
     db.students.insertOne({ name: "Alice", age: 20, hobbies: ["Reading"] })
     ```
   - Expected Output:
     ```
     {
       "acknowledged" : true,
       "insertedId" : ObjectId("671a1234567890abcdef1234")
     }
     ```

2. **Insert Many Documents**:
   - Command: `db.students.insertMany([doc1, doc2])`
   - Description: Inserts multiple at once.
   - Example:
     ```
     db.students.insertMany([
       { name: "Bob", age: 22, hobbies: ["Sports"] },
       { name: "Charlie", age: 21, hobbies: ["Music", "Coding"] }
     ])
     ```
   - Expected Output:
     ```
     {
       "acknowledged" : true,
       "insertedIds" : {
         "0" : ObjectId("671a1234567890abcdef5678"),
         "1" : ObjectId("671a1234567890abcdef9abc")
       }
     }
     ```

3. **Legacy Insert (For Reference)**:
   - Command: `db.students.insert({ name: "David", age: 19 })`
   - Description: Older way, but works—use modern ones instead.

**Tip for Beginners:** Every document gets an auto `_id`. Re-run `db.students.countDocuments({})` – should be `3` or more now.

## Step 4: Query & Read Commands – Fetching Data
Now query the data.

1. **Find All Documents**:
   - Command: `db.students.find()`
   - Description: Returns all documents.
   - Run it (add `.pretty()` for better formatting):
     ```
     db.students.find().pretty()
     ```
   - Expected Output: Shows all inserted docs.

2. **Find with Filter**:
   - Command: `db.students.find({ field: value })`
   - Example:
     ```
     db.students.find({ age: { $gt: 20 } }).pretty()
     ```
   - Expected Output: Docs where age > 20 (e.g., Bob and Charlie).

3. **Find One**:
   - Command: `db.students.findOne({ name: "Alice" })`
   - Description: Returns the first match.
   - Expected Output: Alice's doc.

4. **Projection**:
   - Command: `db.students.find({}, { name: 1, _id: 0 })`
   - Description: Shows only "name" field, excludes "_id".

5. **Sorting**:
   - Command: `db.students.find().sort({ age: -1 })`
   - Description: Sorts descending by age.

6. **Limit & Skip**:
   - Command: `db.students.find().limit(2).skip(1)`
   - Description: Skips first, limits to 2.

7. **Cursor Methods** (For Large Results):
   - Example: Iterate with forEach.
     ```
     db.students.find().forEach(doc => printjson(doc))
     ```

**Tip for Beginners:** `find()` returns a cursor—use methods to control output.

## Step 5: Update Commands – Modifying Data
Update existing docs.

1. **Update One**:
   - Command: `db.students.updateOne(filter, update)`
   - Example:
     ```
     db.students.updateOne(
       { name: "Alice" },
       { $set: { age: 21 }, $push: { hobbies: "Coding" } }
     )
     ```
   - Expected Output: `{ "matchedCount" : 1, "modifiedCount" : 1 }`

2. **Update Many**:
   - Command: `db.students.updateMany(filter, update)`
   - Example (increment ages):
     ```
     db.students.updateMany(
       { age: { $gt: 20 } },
       { $inc: { age: 1 } }
     )
     ```

3. **Replace One**:
   - Command: `db.students.replaceOne(filter, replacement)`
   - Example: Replace Bob's doc entirely.
     ```
     db.students.replaceOne(
       { name: "Bob" },
       { name: "Bob", age: 23, hobbies: ["Gaming"] }
     )
     ```

4. **Upsert**:
   - Add `{ upsert: true }` to insert if no match.

**Tip for Beginners:** Use operators like `$set` to avoid overwriting whole docs. Verify with `find()`.

## Step 6: Delete Commands – Removing Data
Clean up.

1. **Delete One**:
   - Command: `db.students.deleteOne(filter)`
   - Example:
     ```
     db.students.deleteOne({ name: "Charlie" })
     ```
   - Expected Output: `{ "deletedCount" : 1 }`

2. **Delete Many**:
   - Command: `db.students.deleteMany(filter)`
   - Example (delete all under 21):
     ```
     db.students.deleteMany({ age: { $lt: 21 } })
     ```

3. **Legacy Remove**:
   - Command: `db.students.remove({ name: "David" }, { justOne: true })`

**Tip for Beginners:** Always use a filter to avoid deleting everything! Verify with `countDocuments()`.

## Final Cleanup (Optional)
- Drop Collection: `db.students.drop()`
- Drop Database: `db.dropDatabase()`

