 
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

db.students.insertMany([
  { name: "Aaron", age: 18, major: "Computer Science", gpa: 3.1, graduationYear: 2027, address: { city: "San Diego", zip: "92101" }, status: "active", hobbies: ["Coding"] },
  { name: "Bella", age: 21, major: "Math", gpa: 3.6, graduationYear: 2025, address: { city: "Columbus", zip: "43004" }, status: "active", hobbies: ["Reading"] },
  { name: "Caleb", age: 22, major: "Physics", gpa: 2.8, graduationYear: 2024, address: { city: "Charlotte", zip: "28201" }, status: "probation", hobbies: ["Gaming"] },
  { name: "Delilah", age: 20, major: "Biology", gpa: 3.9, graduationYear: 2026, address: { city: "Detroit", zip: "48201" }, status: "active", hobbies: ["Music"] },
  { name: "Ethan", age: 23, major: "Economics", gpa: 3.2, graduationYear: 2023, address: { city: "Memphis", zip: "37501" }, status: "inactive", hobbies: ["Sports"] },
  { name: "Fiona", age: 19, major: "Chemistry", gpa: 3.7, graduationYear: 2027, address: { city: "Baltimore", zip: "21201" }, status: "active", hobbies: ["Reading", "Travel"] },
  { name: "George", age: 24, major: "Computer Science", gpa: 3.4, graduationYear: 2023, address: { city: "Nashville", zip: "37011" }, status: "active", hobbies: ["Chess"] },
  { name: "Hannah", age: 22, major: "Physics", gpa: 3.8, graduationYear: 2024, address: { city: "Louisville", zip: "40201" }, status: "active", hobbies: ["Music", "Coding"] },
  { name: "Isaac", age: 20, major: "Math", gpa: 2.9, graduationYear: 2026, address: { city: "Milwaukee", zip: "53201" }, status: "probation", hobbies: ["Gaming"] },
  { name: "Julia", age: 21, major: "Biology", gpa: 3.5, graduationYear: 2025, address: { city: "Albuquerque", zip: "87101" }, status: "active", hobbies: ["Travel"] },

  { name: "Kevin", age: 23, major: "Chemistry", gpa: 3.0, graduationYear: 2024, address: { city: "Tucson", zip: "85701" }, status: "inactive", hobbies: ["Sports"] },
  { name: "Lily", age: 19, major: "Economics", gpa: 3.9, graduationYear: 2027, address: { city: "Fresno", zip: "93650" }, status: "active", hobbies: ["Reading"] },
  { name: "Mason", age: 22, major: "Computer Science", gpa: 3.3, graduationYear: 2025, address: { city: "Sacramento", zip: "94203" }, status: "active", hobbies: ["Coding", "Gaming"] },
  { name: "Nora", age: 20, major: "Math", gpa: 3.4, graduationYear: 2026, address: { city: "Kansas City", zip: "64101" }, status: "active", hobbies: ["Music"] },
  { name: "Owen", age: 24, major: "Physics", gpa: 2.7, graduationYear: 2023, address: { city: "Mesa", zip: "85201" }, status: "probation", hobbies: ["Sports"] },
  { name: "Paula", age: 21, major: "Biology", gpa: 3.6, graduationYear: 2025, address: { city: "Omaha", zip: "68101" }, status: "active", hobbies: ["Travel"] },
  { name: "Quentin", age: 22, major: "Chemistry", gpa: 3.5, graduationYear: 2024, address: { city: "Raleigh", zip: "27601" }, status: "active", hobbies: ["Reading"] },
  { name: "Rachel", age: 19, major: "Computer Science", gpa: 3.8, graduationYear: 2027, address: { city: "Miami", zip: "33101" }, status: "active", hobbies: ["Coding"] },
  { name: "Samuel", age: 23, major: "Economics", gpa: 3.2, graduationYear: 2023, address: { city: "Cleveland", zip: "44101" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Tina", age: 20, major: "Math", gpa: 3.7, graduationYear: 2026, address: { city: "Virginia Beach", zip: "23450" }, status: "active", hobbies: ["Music"] },

  { name: "Uma", age: 21, major: "Physics", gpa: 3.1, graduationYear: 2025, address: { city: "Oakland", zip: "94601" }, status: "active", hobbies: ["Travel"] },
  { name: "Victor", age: 22, major: "Biology", gpa: 2.9, graduationYear: 2024, address: { city: "Minneapolis", zip: "55401" }, status: "probation", hobbies: ["Sports"] },
  { name: "Wendy", age: 19, major: "Chemistry", gpa: 3.6, graduationYear: 2027, address: { city: "Tulsa", zip: "74101" }, status: "active", hobbies: ["Reading"] },
  { name: "Xavier", age: 23, major: "Computer Science", gpa: 3.4, graduationYear: 2023, address: { city: "Arlington", zip: "76001" }, status: "active", hobbies: ["Coding"] },
  { name: "Yara", age: 20, major: "Economics", gpa: 3.5, graduationYear: 2026, address: { city: "New Orleans", zip: "70112" }, status: "active", hobbies: ["Music"] },
  { name: "Zane", age: 24, major: "Math", gpa: 3.0, graduationYear: 2023, address: { city: "Wichita", zip: "67201" }, status: "inactive", hobbies: ["Gaming"] },

  { name: "Aisha", age: 21, major: "Biology", gpa: 3.7, graduationYear: 2025, address: { city: "Bakersfield", zip: "93301" }, status: "active", hobbies: ["Travel"] },
  { name: "Brandon", age: 22, major: "Physics", gpa: 3.2, graduationYear: 2024, address: { city: "Tampa", zip: "33601" }, status: "active", hobbies: ["Sports"] },
  { name: "Catherine", age: 20, major: "Chemistry", gpa: 3.9, graduationYear: 2026, address: { city: "Aurora", zip: "80010" }, status: "active", hobbies: ["Reading"] },
  { name: "Derek", age: 23, major: "Computer Science", gpa: 3.3, graduationYear: 2023, address: { city: "Anaheim", zip: "92801" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Elena", age: 19, major: "Math", gpa: 3.8, graduationYear: 2027, address: { city: "Honolulu", zip: "96801" }, status: "active", hobbies: ["Music"] },

  { name: "Farhan", age: 22, major: "Economics", gpa: 3.4, graduationYear: 2024, address: { city: "Santa Ana", zip: "92701" }, status: "active", hobbies: ["Travel"] },
  { name: "Gabriella", age: 21, major: "Physics", gpa: 3.6, graduationYear: 2025, address: { city: "Riverside", zip: "92501" }, status: "active", hobbies: ["Reading"] },
  { name: "Harold", age: 24, major: "Chemistry", gpa: 2.8, graduationYear: 2023, address: { city: "Corpus Christi", zip: "78401" }, status: "probation", hobbies: ["Sports"] },
  { name: "Isabella", age: 20, major: "Biology", gpa: 3.9, graduationYear: 2026, address: { city: "Lexington", zip: "40507" }, status: "active", hobbies: ["Music"] },
  { name: "Jonah", age: 23, major: "Computer Science", gpa: 3.5, graduationYear: 2023, address: { city: "Stockton", zip: "95201" }, status: "active", hobbies: ["Coding"] },

  { name: "Kylie", age: 19, major: "Math", gpa: 3.6, graduationYear: 2027, address: { city: "Henderson", zip: "89002" }, status: "active", hobbies: ["Reading"] },
  { name: "Landon", age: 22, major: "Economics", gpa: 3.1, graduationYear: 2024, address: { city: "Saint Paul", zip: "55101" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Monica", age: 21, major: "Physics", gpa: 3.7, graduationYear: 2025, address: { city: "St. Louis", zip: "63101" }, status: "active", hobbies: ["Travel"] },
  { name: "Noah", age: 20, major: "Chemistry", gpa: 3.4, graduationYear: 2026, address: { city: "Cincinnati", zip: "45201" }, status: "active", hobbies: ["Sports"] },
  { name: "Olga", age: 24, major: "Biology", gpa: 3.2, graduationYear: 2023, address: { city: "Pittsburgh", zip: "15201" }, status: "inactive", hobbies: ["Music"] },

  { name: "Peter", age: 23, major: "Computer Science", gpa: 3.8, graduationYear: 2024, address: { city: "Greensboro", zip: "27401" }, status: "active", hobbies: ["Coding"] },
  { name: "Queenie", age: 19, major: "Math", gpa: 3.5, graduationYear: 2027, address: { city: "Anchorage", zip: "99501" }, status: "active", hobbies: ["Reading"] },
  { name: "Rohan", age: 21, major: "Physics", gpa: 3.3, graduationYear: 2025, address: { city: "Plano", zip: "75023" }, status: "active", hobbies: ["Gaming"] },
  { name: "Sophia", age: 22, major: "Economics", gpa: 3.9, graduationYear: 2024, address: { city: "Lincoln", zip: "68501" }, status: "active", hobbies: ["Travel"] },
  { name: "Thomas", age: 24, major: "Chemistry", gpa: 2.9, graduationYear: 2023, address: { city: "Orlando", zip: "32801" }, status: "probation", hobbies: ["Sports"] }
]);


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




