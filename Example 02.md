## Complete script** to **create a `users` collection** and **insert realistic sample data** that you can use to test all the `$regex` examples from earlier.

---

### Step 1: Create & Populate the Collection (Run in `mongosh`)

```js
// Switch to (or create) the database
use mydb;

// Drop existing collection (optional, for clean start)
db.users.drop();

// Insert sample data
db.users.insertMany([
  {
    _id: 1,
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    status: "active",
    role: "admin",
    tags: ["dev", "frontend", "react"],
    createdAt: new ISODate("2023-01-15T10:30:00Z")
  },
  {
    _id: 2,
    name: "bob smith",
    email: "BOB.SMITH@EXAMPLE.COM",
    status: "inactive",
    role: "user",
    tags: ["marketing", "seo"],
    createdAt: new ISODate("2023-02-20T14:22:11Z")
  },
  {
    _id: 3,
    name: "Charlie Brown",
    email: "charlie@peanuts.org",
    status: "active",
    role: "editor",
    tags: ["content", "blog", "peanuts"],
    createdAt: new ISODate("2023-03-10T09:15:45Z")
  },
  {
    _id: 4,
    name: "Diana Prince",
    email: "diana@amazon.heroes",
    status: "active",
    role: "superhero",
    tags: ["justice", "wonder", "dc"],
    createdAt: new ISODate("2023-04-05T18:00:00Z")
  },
  {
    _id: 5,
    name: "Eve Adams",
    email: "eve.adams@techstart.io",
    status: "pending",
    role: "user",
    tags: ["startup", "python", "ai"],
    createdAt: new ISODate("2023-05-12T11:11:11Z")
  },
  {
    _id: 6,
    name: "Frank Miller",
    email: "frank.miller@darkknight.com",
    status: "active",
    role: "artist",
    tags: ["comics", "batman", "graphic-novel"],
    createdAt: new ISODate("2023-06-18T22:45:30Z")
  },
  {
    _id: 7,
    name: "Grace Hopper",
    email: "grace@navy.mil",
    status: "active",
    role: "pioneer",
    tags: ["cobol", "compiler", "legend"],
    createdAt: new ISODate("2023-07-01T08:00:00Z")
  },
  {
    _id: 8,
    name: "Henry Ford",
    email: "henry@fordmotors.co",
    status: "inactive",
    role: "founder",
    tags: ["automobile", "assembly-line"],
    createdAt: new ISODate("2023-08-25T16:20:00Z")
  },
  {
    _id: 9,
    name: "Iris West",
    email: "iris@centralcity.news",
    status: "active",
    role: "reporter",
    tags: ["flash", "journalism", "dc"],
    createdAt: new ISODate("2023-09-14T13:37:22Z")
  },
  {
    _id: 10,
    name: "Jack Ryan",
    email: "jack.ryan@cia.gov",
    status: "active",
    role: "analyst",
    tags: ["thriller", "espionage", "tom-clancy"],
    createdAt: new ISODate("2023-10-01T05:55:55Z")
  }
]);

// Confirm insertion
print(`Inserted ${db.users.countDocuments({})} documents into 'users' collection.`);
```

---

### Step 2: Create Useful Indexes (Optional but Recommended)

```js
// Case-insensitive index on name (for prefix searches)
db.users.createIndex({ name: 1 });

// Index on email
db.users.createIndex({ email: 1 });

// Index on status
db.users.createIndex({ status: 1 });

// Text index on name and tags (for $text search, alternative to regex)
db.users.createIndex({ name: "text", tags: "text" });
```

---

### Verify Data

```js
db.users.find().pretty();
```

**Sample Output (truncated):**

```json
{
  "_id" : 1,
  "name" : "Alice Johnson",
  "email" : "alice.johnson@example.com",
  "status" : "active",
  "role" : "admin",
  ...
}
```

---

### Now Test `$regex` Queries!

#### Example 1: Find users with name starting with "A" (case-insensitive)

```js
db.users.find({ name: { $regex: /^a/i } }).pretty();
```

**Matches:** Alice Johnson

---

#### Example 2: Emails ending with `.com`

```js
db.users.find({ email: { $regex: /\.com$/i } }).pretty();
```

**Matches:** Alice, Bob, Frank

---

#### Example 3: Contains "wonder" in tags

```js
db.users.find({ tags: { $regex: /wonder/i } }).pretty();
```

**Matches:** Diana Prince

---

#### Example 4: Exact word "active" in status

```js
db.users.find({ status: { $regex: '^active$', $options: 'i' } }).pretty();
```

-------------------

# MongoDB Aggregation Pipeline

- `$match` → Filter
- `$group` → Group & calculate
- `$project` → Select/show fields
- `$sort` → Sort results
- `$limit` → Limit output

---

### Sample Data (We’ll use the `users` collection from before)

```js
[
  { name: "Alice", dept: "IT", salary: 7000 },
  { name: "Bob",   dept: "HR", salary: 5000 },
  { name: "Charlie", dept: "IT", salary: 8000 },
  { name: "Diana", dept: "HR", salary: 5500 },
  { name: "Eve",   dept: "IT", salary: 7500 }
]
```

---

## Goal:
> **"Find average salary per department, but only for departments with average salary > 6000, and show top 2 departments by average salary."**

---

## Aggregation Pipeline (Step-by-step)

```js
db.users.aggregate([
  // Step 1: FILTER - Keep only IT and HR (example filter)
  {
    $match: { dept: { $in: ["IT", "HR"] } }
  },

  // Step 2: GROUP - Group by department, calculate avg salary
  {
    $group: {
      _id: "$dept",                    // Group by department
      avgSalary: { $avg: "$salary" },  // Average salary
      totalEmployees: { $sum: 1 }      // Count employees
    }
  },

  // Step 3: FILTER AGAIN - Only depts with avg > 6000
  {
    $match: { avgSalary: { $gt: 6000 } }
  },

  // Step 4: PROJECT - Rename and format output
  {
    $project: {
      _id: 0,                         // Hide _id
      department: "$_id",             // Rename _id → department
      averageSalary: { $round: ["$avgSalary", 2] },  // Round to 2 decimals
      employeeCount: "$totalEmployees"
    }
  },

  // Step 5: SORT - Highest average salary first
  {
    $sort: { averageSalary: -1 }
  },

  // Step 6: LIMIT - Show only top 2
  {
    $limit: 2
  }
])
```

---

## Output (Easy to Read)

```json
[
  {
    "department": "IT",
    "averageSalary": 7500,
    "employeeCount": 3
  },
  {
    "department": "HR",
    "averageSalary": 5250,
    "employeeCount": 2
  }
]
```

> Only **IT** appears because HR avg (5250) is **not > 6000**.

---

## Each Stage Explained (Super Simple)

| Stage        | What it does                              | Like SQL |
|-------------|-------------------------------------------|---------|
| `$match`    | Filters documents (like `WHERE`)          | `WHERE dept IN ('IT','HR')` |
| `$group`    | Groups and calculates (like `GROUP BY`)   | `GROUP BY dept` |
| `$project`  | Picks or reshapes fields (like `SELECT`)  | `SELECT dept, AVG(salary)` |
| `$sort`     | Orders results                            | `ORDER BY avgSalary DESC` |
| `$limit`    | Shows only first N results                | `LIMIT 2` |

---

## Try This Now! (Copy-Paste in `mongosh`)

```js
// First, insert sample data
db.users.drop();
db.users.insertMany([
  { name: "Alice", dept: "IT", salary: 7000 },
  { name: "Bob", dept: "HR", salary: 5000 },
  { name: "Charlie", dept: "IT", salary: 8000 },
  { name: "Diana", dept: "HR", salary: 5500 },
  { name: "Eve", dept: "IT", salary: 7500 }
]);

// Then run the pipeline
db.users.aggregate([
  { $match: { dept: { $in: ["IT", "HR"] } } },
  { $group: { _id: "$dept", avgSalary: { $avg: "$salary" }, totalEmployees: { $sum: 1 } } },
  { $match: { avgSalary: { $gt: 6000 } } },
  { $project: { _id: 0, department: "$_id", averageSalary: { $round: ["$avgSalary", 2] }, employeeCount: "$totalEmployees" } },
  { $sort: { averageSalary: -1 } },
  { $limit: 2 }
]).pretty();
```

---

## Bonus: Visual Flow

```
All Docs
   ↓ $match → only IT & HR
   ↓ $group → avg salary per dept
   ↓ $match → avg > 6000
   ↓ $project → clean output
   ↓ $sort → high to low
   ↓ $limit → top 2
```

---

**You're now an aggregation beginner pro!**

Try changing:
- `$match` → add `salary > 6000`
- `$group` → use `$sum`, `$max`, `$min`
- `$project` → add `1` or `0` to show/hide fields



