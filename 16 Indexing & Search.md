# MongoDB Index and Search

MongoDB indexes improve query performance by allowing MongoDB to quickly locate documents without scanning the entire collection.

## Step 1: Create a Database

```javascript
use schoolDB
```

## Step 2: Create a Collection

```javascript
db.students.insertMany([
  {
    name: "Pankaj",
    age: 25,
    city: "Indore"
  },
  {
    name: "Rahul",
    age: 22,
    city: "Mumbai"
  },
  {
    name: "Priya",
    age: 24,
    city: "Delhi"
  },
  {
    name: "Amit",
    age: 23,
    city: "Mumbai"
  }
])
```

---

# Search Without Index

Suppose you want to find students from Mumbai.

```javascript
db.students.find({ city: "Mumbai" })
```

Output:

```javascript
{ name: "Rahul", age: 22, city: "Mumbai" }
{ name: "Amit", age: 23, city: "Mumbai" }
```

Without an index, MongoDB performs a **Collection Scan (COLLSCAN)** and checks every document.

---

# Step 3: Create an Index

Create an index on the `city` field:

```javascript
db.students.createIndex({ city: 1 })
```

Output:

```javascript
city_1
```

Here:

* `1` = Ascending order
* `-1` = Descending order

---

# Step 4: View Indexes

```javascript
db.students.getIndexes()
```

Example Output:

```javascript
[
  {
    key: { _id: 1 },
    name: "_id_"
  },
  {
    key: { city: 1 },
    name: "city_1"
  }
]
```

---

# Step 5: Search Using Index

Run the same query:

```javascript
db.students.find({ city: "Mumbai" })
```

MongoDB now uses the `city` index to locate matching documents much faster.

---

# Step 6: Verify Index Usage

Use `explain()`:

```javascript
db.students.find({ city: "Mumbai" }).explain("executionStats")
```

Look for:

```javascript
"stage": "IXSCAN"
```

Meaning:

* `IXSCAN` = Index Scan (Good)
* `COLLSCAN` = Collection Scan (Slow)

---

# Compound Index Example

Suppose you frequently search by city and age together.

Create a compound index:

```javascript
db.students.createIndex({
  city: 1,
  age: 1
})
```

Search:

```javascript
db.students.find({
  city: "Mumbai",
  age: 22
})
```

MongoDB can use the compound index for faster searching.

---

# Text Search Example

Insert documents:

```javascript
db.articles.insertMany([
  {
    title: "Learn MongoDB",
    content: "MongoDB is a NoSQL database"
  },
  {
    title: "Python Tutorial",
    content: "Python is easy to learn"
  }
])
```

Create a text index:

```javascript
db.articles.createIndex({
  title: "text",
  content: "text"
})
```

Search for a word:

```javascript
db.articles.find({
  $text: {
    $search: "MongoDB"
  }
})
```

Output:

```javascript
{
  title: "Learn MongoDB",
  content: "MongoDB is a NoSQL database"
}
```

---

# Remove an Index

View indexes:

```javascript
db.students.getIndexes()
```

Drop the index:

```javascript
db.students.dropIndex("city_1")
```

---

# Summary

| Operation         | Command                                |
| ----------------- | -------------------------------------- |
| Create Index      | `db.collection.createIndex({field:1})` |
| View Indexes      | `db.collection.getIndexes()`           |
| Search Data       | `db.collection.find()`                 |
| Check Index Usage | `.explain("executionStats")`           |
| Create Text Index | `createIndex({field:"text"})`          |
| Text Search       | `$text: {$search:"keyword"}`           |
| Delete Index      | `dropIndex()`                          |

### Why Use Indexes?

* Faster searches
* Faster sorting
* Better query performance
* Essential for large collections with thousands or millions of documents

**Rule of Thumb:** Create indexes on fields that are frequently used in `find()`, `sort()`, and filtering operations.
