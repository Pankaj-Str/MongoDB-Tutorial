# Query & Projection Operators –

---

## Step 1: Setup – Insert Sample Data

Run this in `mongosh` after `use school`:

```js
db.students.drop()
db.students.insertMany([
  {
    name: "Alice",
    age: 20,
    major: "Computer Science",
    gpa: 3.8,
    enrolled: true,
    hobbies: ["coding", "gaming"],
    address: { city: "New York", zip: "10001" },
    scores: [95, 88, 92],
    graduationYear: 2026,
    status: "active"
  },
  {
    name: "Bob",
    age: 22,
    major: "Biology",
    gpa: 3.5,
    enrolled: true,
    hobbies: ["reading", "hiking"],
    address: { city: "Boston", zip: "02101" },
    scores: [78, 85, 80],
    graduationYear: 2025,
    status: "active"
  },
  {
    name: "Charlie",
    age: 19,
    major: "Math",
    gpa: 4.0,
    enrolled: false,
    hobbies: ["chess"],
    address: { city: "Chicago", zip: null },
    scores: [100, 98, 99],
    graduationYear: null,
    status: "inactive"
  },
  {
    name: "Diana",
    age: 21,
    major: "Physics",
    gpa: 3.9,
    enrolled: true,
    hobbies: ["gaming", "painting"],
    address: { city: "New York", zip: "10002" },
    scores: [90, 92, 88],
    graduationYear: 2026,
    status: "active"
  },
  {
    name: "Eve",
    age: 23,
    major: "Computer Science",
    gpa: null,
    enrolled: true,
    hobbies: [],
    address: { city: "Seattle" },
    scores: [],
    graduationYear: 2025,
    status: "probation"
  }
])
```

---

## Step 2: **Comparison Operators** – Full Examples

| Operator | Meaning             | Example Query                                                                                   | Result Explanation |
|---------|---------------------|--------------------------------------------------------------------------------------------------|--------------------|
| `$eq`   | Equals              | `db.students.find({ age: { $eq: 20 } }).pretty()`                                               | Alice only         |
| `$ne`   | Not equals          | `db.students.find({ major: { $ne: "Computer Science" } }).pretty()`                             | Bob, Charlie, Diana |
| `$gt`   | Greater than        | `db.students.find({ age: { $gt: 21 } }).pretty()`                                               | Bob, Eve           |
| `$gte`  | Greater than or equal | `db.students.find({ gpa: { $gte: 3.8 } }).pretty()`                                           | Alice, Diana, Charlie |
| `$lt`   | Less than           | `db.students.find({ age: { $lt: 20 } }).pretty()`                                               | Charlie            |
| `$lte`  | Less than or equal  | `db.students.find({ age: { $lte: 20 } }).pretty()`                                              | Alice, Charlie     |
| `$in`   | In array            | `db.students.find({ major: { $in: ["Computer Science", "Physics"] } }).pretty()`                | Alice, Diana, Eve  |
| `$nin`  | Not in array        | `db.students.find({ status: { $nin: ["active", "inactive"] } }).pretty()`                       | Eve (probation)    |

---

## Step 3: **Logical Operators** – Full Examples

| Operator | Meaning             | Example Query                                                                                   | Result |
|---------|---------------------|--------------------------------------------------------------------------------------------------|--------|
| `$and`  | All conditions true | `db.students.find({ $and: [ { age: { $gt: 20 } }, { gpa: { $gte: 3.5 } } ] }).pretty()`           | Bob, Diana |
| `$or`   | Any condition true  | `db.students.find({ $or: [ { major: "Math" }, { gpa: 4.0 } ] }).pretty()`                        | Charlie (both) |
| `$not`  | Negates expression  | `db.students.find({ age: { $not: { $lt: 21 } } }).pretty()`                                      | Bob, Eve (age ≥ 21) |
| `$nor`  | None true           | `db.students.find({ $nor: [ { major: "Math" }, { gpa: 4.0 } ] }).pretty()`                       | All except Charlie |

> **Note**: `$not` applies to a single field expression. Use `$nor` or `$and` with `$ne` for multiple negations.

---

## Step 4: **Element Operators** – Full Examples

| Operator  | Meaning               | Example Query                                                                                   | Result |
|-----------|-----------------------|--------------------------------------------------------------------------------------------------|--------|
| `$exists` | Field exists          | `db.students.find({ graduationYear: { $exists: true } }).pretty()`                              | Alice, Bob, Diana, Eve |
|           |                       | `db.students.find({ graduationYear: { $exists: false } }).pretty()`                             | Charlie |
| `$type`   | Field is specific type| `db.students.find({ gpa: { $type: "double" } }).pretty()`                                        | Alice, Bob, Diana |
|           |                       | `db.students.find({ gpa: { $type: "null" } }).pretty()`                                          | Eve |
|           |                       | `db.students.find({ "address.zip": { $type: "string" } }).pretty()`                             | Alice, Bob, Diana |
|           |                       | `db.students.find({ "address.zip": { $type: "null" } }).pretty()`                               | Charlie |

> **Common BSON Types**: `"double"`, `"string"`, `"object"`, `"array"`, `"bool"`, `"null"`, `"int"`, `"date"`, etc.

---

## Step 5: **Projection Examples** – Control Output Fields

Projection uses the **second argument** in `.find()` to include/exclude fields.

```js
// 1. Include only name and gpa, exclude _id
db.students.find({}, { name: 1, gpa: 1, _id: 0 }).pretty()
```

**Output**:
```json
{ "name": "Alice", "gpa": 3.8 }
{ "name": "Bob", "gpa": 3.5 }
...
```

```js
// 2. Include nested field, exclude others
db.students.find({}, { "address.city": 1, _id: 0 }).pretty()
```

**Output**:
```json
{ "address": { "city": "New York" } }
{ "address": { "city": "Boston" } }
...
```

```js
// 3. Include array element (first match) using $elemMatch in projection
db.students.find(
  { hobbies: "gaming" },
  { name: 1, hobbies: { $elemMatch: { $eq: "gaming" } }, _id: 0 }
).pretty()
```

**Output**:
```json
{ "name": "Alice", "hobbies": [ "gaming" ] }
{ "name": "Diana", "hobbies": [ "gaming" ] }
```

```js
// 4. Use $slice to limit array elements
db.students.find(
  { scores: { $exists: true, $ne: [] } },
  { name: 1, scores: { $slice: 2 }, _id: 0 }
).pretty()
```

**Output**:
```json
{ "name": "Alice", "scores": [ 95, 88 ] }
{ "name": "Bob", "scores": [ 78, 85 ] }
```

---

## Step 6: **Advanced Query: Combine Everything**

**Find active students in New York with GPA > 3.7, return name and first 2 scores:**

```js
db.students.find(
  {
    status: "active",
    "address.city": "New York",
    gpa: { $gt: 3.7 },
    enrolled: true
  },
  {
    name: 1,
    gpa: 1,
    scores: { $slice: 2 },
    "address.city": 1,
    _id: 0
  }
).pretty()
```

**Output**:
```json
{
  "name": "Alice",
  "gpa": 3.8,
  "address": { "city": "New York" },
  "scores": [ 95, 88 ]
}
{
  "name": "Diana",
  "gpa": 3.9,
  "address": { "city": "New York" },
  "scores": [ 90, 92 ]
}
```

---

## Summary Table: All Operators Covered

| Category     | Operators |
|--------------|---------|
| **Comparison** | `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin` |
| **Logical**    | `$and`, `$or`, `$not`, `$nor` |
| **Element**    | `$exists`, `$type` |
| **Projection** | Field inclusion (`field: 1`), exclusion (`field: 0`), `$elemMatch`, `$slice` |

---

## Pro Tips

- Use **indexes** on frequently queried fields:  
  ```js
  db.students.createIndex({ age: 1 })
  db.students.createIndex({ "address.city": 1 })
  ```
- Use `.explain("executionStats")` to check query performance.
- Always **project only needed fields** in production to reduce network/data load.

---

