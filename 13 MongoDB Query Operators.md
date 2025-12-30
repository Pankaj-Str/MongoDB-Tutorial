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

# MongoDB Query & Projection Operators – One Clear Example for Each Operator

We’ll use the same **students** collection from before (in the `school` database).  
If you haven’t inserted the data yet, run the setup from the previous message first.


### Comparison Operators

```javascript
// $eq – Matches values that are equal
db.students.find({ age: { $eq: 21 } }).pretty()
// Result: Diana only
```

```javascript
// $ne – Not equal
db.students.find({ major: { $ne: "Computer Science" } }).pretty()
// Result: Bob, Charlie, Diana
```

```javascript
// $gt – Greater than
db.students.find({ gpa: { $gt: 3.7 } }).pretty()
// Result: Alice (3.8), Charlie (4.0), Diana (3.9)
```

```javascript
// $gte – Greater than or equal
db.students.find({ age: { $gte: 22 } }).pretty()
// Result: Bob (22), Eve (23)
```

```javascript
// $lt – Less than
db.students.find({ age: { $lt: 20 } }).pretty()
// Result: Charlie (19)
```

```javascript
// $lte – Less than or equal
db.students.find({ gpa: { $lte: 3.5 } }).pretty()
// Result: Bob (3.5)
```

```javascript
// $in – Matches any value in the list
db.students.find({ name: { $in: ["Alice", "Eve"] } }).pretty()
// Result: Alice and Eve
```

```javascript
// $nin – Does NOT match any value in the list
db.students.find({ status: { $nin: ["active"] } }).pretty()
// Result: Charlie (inactive), Eve (probation)
```

### Logical Operators

```javascript
// $and – All conditions must be true
db.students.find({ $and: [{ enrolled: true }, { age: { $gt: 20 } }] }).pretty()
// Result: Bob, Diana, Eve
```

```javascript
// $or – At least one condition true
db.students.find({ $or: [{ major: "Math" }, { gpa: 4.0 }] }).pretty()
// Result: Charlie (has both)
```

```javascript
// $not – Reverses the condition
db.students.find({ age: { $not: { $lt: 21 } } }).pretty()
// Result: Students age 21 or older → Bob (22), Diana (21), Eve (23)
```

```javascript
// $nor – None of the conditions are true
db.students.find({ $nor: [{ major: "Physics" }, { major: "Math" }] }).pretty()
// Result: Everyone except Diana and Charlie
```

### Element Operators

```javascript
// $exists: true – Field is present
db.students.find({ "address.zip": { $exists: true } }).pretty()
// Result: Alice, Bob, Diana (they have zip)
```

```javascript
// $exists: false – Field is missing
db.students.find({ "address.zip": { $exists: false } }).pretty()
// Result: Charlie (zip: null), Eve (no zip field)
```

```javascript
// $type – Field has specific data type
db.students.find({ gpa: { $type: "null" } }).pretty()
// Result: Eve (gpa is null)
```

```javascript
// $type example with array
db.students.find({ hobbies: { $type: "array" } }).pretty()
// Result: All students (even empty array counts as array)
```

### Array Operators (in Query)

```javascript
// Exact array match
db.students.find({ hobbies: ["coding", "gaming"] }).pretty()
// Result: Alice only (exact order and contents)
```

```javascript
// $all – Array contains ALL these elements (order doesn't matter)
db.students.find({ hobbies: { $all: ["gaming", "painting"] } }).pretty()
// Result: Diana
```

```javascript
// $size – Array has exact number of elements
db.students.find({ scores: { $size: 3 } }).pretty()
// Result: Alice, Bob, Charlie, Diana
```

```javascript
// $elemMatch – Array element satisfies multiple conditions
db.students.find({ scores: { $elemMatch: { $gte: 95, $lte: 100 } } }).pretty()
// Result: Alice (has 95), Charlie (has 100,98,99)
```

### Projection Operators

```javascript
// Include specific fields (and hide _id)
db.students.find({ enrolled: true }, { name: 1, gpa: 1, _id: 0 }).pretty()
// Shows only name and gpa for enrolled students
```

```javascript
// Exclude specific fields
db.students.find({}, { scores: 0, hobbies: 0 }).pretty()
// Hides scores and hobbies from all results
```

```javascript
// $slice – Return only first N elements of array
db.students.find({}, { name: 1, scores: { $slice: 2 }, _id: 0 }).pretty()
// Shows name and first 2 scores only
```

```javascript
// $elemMatch in projection – Return only matching array elements
db.students.find(
  { hobbies: "gaming" },
  { name: 1, hobbies: { $elemMatch: { $eq: "gaming" } }, _id: 0 }
).pretty()
// Shows only ["gaming"] in hobbies for Alice and Diana
```

```javascript
// Nested field projection
db.students.find({}, { "address.city": 1, _id: 0 }).pretty()
// Shows only the city inside address
```

