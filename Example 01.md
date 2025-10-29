 
# Step-by-Step with Real Commands


---

```markdown
# MongoDB Complete Beginner Tutorial  
> **One File, Step-by-Step, Real Commands, Notes, Examples**  
> **Database:** `school` | **Collection:** `students`  
> **Tool:** `mongosh` (MongoDB Shell)  
> **Level:** Absolute Beginner  
> **Goal:** Learn **CRUD + Query Operators** in **one flow**

---

## Table of Contents
1. [Setup & Sample Data](#setup)
2. [Database & Collection Commands](#db-coll)
3. [Insert Documents](#insert)
4. [Query & Read (Find)](#query)
5. [Update Documents](#update)
6. [Delete Documents](#delete)
7. [Query Operators (Comparison, Logical, Element)](#operators)
8. [Cleanup](#cleanup)

---

<a name="setup"></a>
## Step 1: Setup – Open mongosh & Insert Sample Data

```bash
# 1. Open terminal and start MongoDB shell
mongosh
```

```javascript
// 2. Switch to (or create) database: school
use school
// Output: switched to db school
```

```javascript
// 3. (Optional) Drop old data if exists
db.students.drop()
```

```javascript
// 4. Insert 5 rich sample documents
db.students.insertMany([
  {
    name: "Alice",
    age: 20,
    major: "Computer Science",
    gpa: 3.8,
    graduationYear: 2024,
    address: { city: "New York", zip: "10001" },
    status: "active",
    hobbies: ["Reading", "Coding"]
  },
  {
    name: "Bob",
    age: 22,
    major: "Biology",
    gpa: 3.5,
    graduationYear: 2023,
    address: { city: "Boston", zip: "02101" },
    status: "inactive",
    hobbies: ["Sports"]
  },
  {
    name: "Charlie",
    age: 19,
    major: "Math",
    gpa: 4,
    address: { city: "Chicago" },
    status: "active",
    hobbies: ["Music"]
  },
  {
    name: "Diana",
    age: 21,
    major: "Physics",
    gpa: 3.9,
    graduationYear: 2025,
    address: { city: "LA", zip: "90001" },
    status: "active",
    hobbies: ["Gaming", "Reading"]
  },
  {
    name: "Eve",
    age: 23,
    major: "Computer Science",
    gpa: null,
    graduationYear: 2026,
    address: { city: "Seattle", zip: "98101" },
    status: "probation"
  }
])
// Output: { acknowledged: true, insertedIds: { ... } }
```

```javascript
// 5. Verify data
db.students.find().pretty()
```

---

<a name="db-coll"></a>
## Step 2: Database & Collection Commands

```javascript
// Show current database
db
// Output: school
```

```javascript
// List all databases
show dbs
// Output: school 0.000GB
```

```javascript
// List collections
show collections
// Output: students
```

```javascript
// Collection stats
db.students.stats()
// Output: { count: 5, size: ..., ... }
```

```javascript
// Count documents
db.students.countDocuments({})
// Output: 5
```

```javascript
// Estimated count (faster)
db.students.estimatedDocumentCount()
// Output: 5
```

---

<a name="insert"></a>
## Step 3: Insert Commands

```javascript
// Insert one more student
db.students.insertOne({
  name: "Frank",
  age: 20,
  major: "Art",
  gpa: 3.2,
  status: "active"
})
```

```javascript
// Legacy insert (avoid in new code)
db.students.insert({ name: "Grace", age: 18 })
```

---

<a name="query"></a>
## Step 4: Query & Read Commands

```javascript
// Find all
db.students.find().pretty()
```

```javascript
// Find one
db.students.findOne({ name: "Alice" })
```

```javascript
// Filter: age = 20
db.students.find({ age: 20 }).pretty()
```

```javascript
// Projection: only name and major
db.students.find({}, { name: 1, major: 1, _id: 0 }).pretty()
```

```javascript
// Sort by age descending
db.students.find().sort({ age: -1 }).pretty()
```

```javascript
// Limit & skip
db.students.find().sort({ age: 1 }).limit(3).skip(1).pretty()
```

```javascript
// Iterate with cursor
db.students.find().forEach(doc => print(doc.name + " is " + doc.age))
```

---

<a name="update"></a>
## Step 5: Update Commands

```javascript
// Update one: change Alice's age
db.students.updateOne(
  { name: "Alice" },
  { $set: { age: 21 }, $push: { hobbies: "Swimming" } }
)
// Output: modifiedCount: 1
```

```javascript
// Update many: increase GPA by 0.1 for active students
db.students.updateMany(
  { status: "active" },
  { $inc: { gpa: 0.1 } }
)
```

```javascript
// Replace entire document
db.students.replaceOne(
  { name: "Frank" },
  { name: "Frank", age: 21, major: "Design", gpa: 3.7 }
)
```

```javascript
// Upsert: add or update
db.students.updateOne(
  { name: "Henry" },
  { $set: { age: 25, major: "History" } },
  { upsert: true }
)
```

---

<a name="delete"></a>
## Step 6: Delete Commands

```javascript
// Delete one
db.students.deleteOne({ name: "Grace" })
```

```javascript
// Delete many: remove inactive students
db.students.deleteMany({ status: "inactive" })
```

---

<a name="operators"></a>
## Step 7: Query Operators – Full Examples

### Comparison Operators

| Operator | Meaning | Query | Result |
|--------|--------|-------|--------|
| `$eq` | Equals | `db.students.find({ age: { $eq: 21 } }).pretty()` | Alice, Diana, Frank |
| `$ne` | Not equals | `db.students.find({ major: { $ne: "Computer Science" } }).pretty()` | Bob, Charlie, Diana, Henry |
| `$gt` | > | `db.students.find({ age: { $gt: 21 } }).pretty()` | Eve |
| `$gte` | ≥ | `db.students.find({ gpa: { $gte: 3.8 } }).pretty()` | Alice, Diana |
| `$lt` | < | `db.students.find({ age: { $lt: 20 } }).pretty()` | Charlie |
| `$lte` | ≤ | `db.students.find({ age: { $lte: 20 } }).pretty()` | Charlie |
| `$in` | In list | `db.students.find({ major: { $in: ["Math", "Physics"] } }).pretty()` | Charlie, Diana |
| `$nin` | Not in | `db.students.find({ status: { $nin: ["active"] } }).pretty()` | Eve |

---

### Logical Operators

```javascript
// $and: age > 20 AND gpa >= 3.5
db.students.find({
  $and: [
    { age: { $gt: 20 } },
    { gpa: { $gte: 3.5 } }
  ]
}).pretty()
// → Diana, Eve
```

```javascript
// $or: major Math OR gpa = 4
db.students.find({
  $or: [
    { major: "Math" },
    { gpa: 4 }
  ]
}).pretty()
// → Charlie
```

```javascript
// $not: age NOT < 21 → age >= 21
db.students.find({ age: { $not: { $lt: 21 } } }).pretty()
// → Diana, Eve
```

```javascript
// $nor: NOT (major Math OR gpa 4)
db.students.find({
  $nor: [
    { major: "Math" },
    { gpa: 4 }
  ]
}).pretty()
// → All except Charlie
```

---

### Element Operators

```javascript
// $exists: true → field exists
db.students.find({ graduationYear: { $exists: true } }).pretty()
// → Alice, Bob, Diana, Eve
```

```javascript
// $exists: false → field missing
db.students.find({ graduationYear: { $exists: false } }).pretty()
// → Charlie, Frank, Henry
```

```javascript
// $type: "double"
db.students.find({ gpa: { $type: "double" } }).pretty()
// → Alice, Bob, Diana, Frank
```

```javascript
// $type: "null"
db.students.find({ gpa: { $type: "null" } }).pretty()
// → Eve
```

```javascript
// Nested field type
db.students.find({ "address.zip": { $type: "string" } }).pretty()
// → Alice, Bob, Diana, Eve
```

---

<a name="cleanup"></a>
## Step 8: Cleanup (Optional)

```javascript
// Drop collection
db.students.drop()
// Output: true
```

```javascript
// Drop database
db.dropDatabase()
// Output: { dropped: "school", ok: 1 }
```

---

## Final Checklist

| Task | Done? |
|------|-------|
| Created DB & collection | Yes |
| Inserted sample data | Yes |
| Used all CRUD operations | Yes |
| Applied query operators | Yes |
| Cleaned up | Yes |

---




