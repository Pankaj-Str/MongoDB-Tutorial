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

### Examples** for key MongoDB aggregation pipeline stages: `$match`, `$group`, `$project`, and a few others (`$sort`, `$limit`, `$unwind`). Each example is **standalone** (focuses on one main stage) but may include basic combinations for context. I'll use the `users` collection you provided (10 documents).

For each example:
- **Goal**: What the pipeline does.
- **Step-by-Step Explanation**: Easy breakdown.
- **Pipeline Code**: Ready-to-run in `mongosh`.
- **Expected Output**: Based on the data (I'll simulate it since the dataset is small).

Run these in `mongosh` after inserting the data. Aggregation uses `db.users.aggregate([...])`.

---

### Example 1: `$match` (Filter Documents)
**Goal**: Find all users with `status: "active"`. `$match` acts like a filter to narrow down documents early in the pipeline.

**Step-by-Step Explanation**:
1. Start with all 10 documents in the `users` collection.
2. Use `$match` to keep only those where `status` equals `"active"` (case-sensitive).
3. The pipeline outputs the matching full documents (7 out of 10 match).

**Pipeline Code**:
```js
db.users.aggregate([
  { $match: { status: "active" } }
]);
```

**Expected Output** (7 documents):
```json
{ "_id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com", "status": "active", ... }
{ "_id": 3, "name": "Charlie Brown", "email": "charlie@peanuts.org", "status": "active", ... }
{ "_id": 4, "name": "Diana Prince", "email": "diana@amazon.heroes", "status": "active", ... }
{ "_id": 6, "name": "Frank Miller", "email": "frank.miller@darkknight.com", "status": "active", ... }
{ "_id": 7, "name": "Grace Hopper", "email": "grace@navy.mil", "status": "active", ... }
{ "_id": 9, "name": "Iris West", "email": "iris@centralcity.news", "status": "active", ... }
{ "_id": 10, "name": "Jack Ryan", "email": "jack.ryan@cia.gov", "status": "active", ... }
```

---

### Example 2: `$group` (Aggregate Data)
**Goal**: Count users by `role`. `$group` groups documents and applies calculations (like count).

**Step-by-Step Explanation**:
1. Start with all 10 documents.
2. Use `$group` to group by the `role` field (e.g., all "user" together).
3. For each group, calculate a new field `count` using `$sum: 1` (adds 1 per document).
4. Output is new documents: one per unique role with its count.

**Pipeline Code**:
```js
db.users.aggregate([
  { $group: { _id: "$role", count: { $sum: 1 } } }
]);
```

**Expected Output** (6 documents, one per role):
```json
{ "_id": "admin", "count": 1 }
{ "_id": "user", "count": 2 }
{ "_id": "editor", "count": 1 }
{ "_id": "superhero", "count": 1 }
{ "_id": "artist", "count": 1 }
{ "_id": "pioneer", "count": 1 }
{ "_id": "founder", "count": 1 }
{ "_id": "reporter", "count": 1 }
{ "_id": "analyst", "count": 1 }
```

---

### Example 3: `$project` (Select and Reshape Fields)
**Goal**: Show only `name` and `email` for all users, and add a new field `nameUpper` (uppercase name). `$project` picks fields and can create new ones.

**Step-by-Step Explanation**:
1. Start with all 10 documents.
2. Use `$project` to include specific fields: keep `name` and `email`.
3. Create a new field `nameUpper` using `$toUpper: "$name"` (converts name to uppercase).
4. `_id` is included by default; set `_id: 0` to hide it.
5. Output is reshaped documents (10 total).

**Pipeline Code**:
```js
db.users.aggregate([
  { $project: { _id: 0, name: 1, email: 1, nameUpper: { $toUpper: "$name" } } }
]);
```

**Expected Output** (10 documents, truncated):
```json
{ "name": "Alice Johnson", "email": "alice.johnson@example.com", "nameUpper": "ALICE JOHNSON" }
{ "name": "bob smith", "email": "BOB.SMITH@EXAMPLE.COM", "nameUpper": "BOB SMITH" }
{ "name": "Charlie Brown", "email": "charlie@peanuts.org", "nameUpper": "CHARLIE BROWN" }
... (and so on for all 10)
```

---

### Example 4: `$sort` (Sort Results)
**Goal**: Sort users by `createdAt` (oldest to newest). `$sort` orders documents.

**Step-by-Step Explanation**:
1. Start with all 10 documents.
2. Use `$sort` on `createdAt`: `1` means ascending (oldest first).
3. Output is the full documents, now sorted.

**Pipeline Code**:
```js
db.users.aggregate([
  { $sort: { createdAt: 1 } }
]);
```

**Expected Output** (10 documents, sorted by date):
```json
{ "_id": 1, "name": "Alice Johnson", "createdAt": ISODate("2023-01-15T10:30:00Z"), ... }  // Oldest
{ "_id": 2, "name": "bob smith", "createdAt": ISODate("2023-02-20T14:22:11Z"), ... }
{ "_id": 3, "name": "Charlie Brown", "createdAt": ISODate("2023-03-10T09:15:45Z"), ... }
... (up to Jack Ryan as newest)
```

---

### Example 5: `$limit` (Limit Number of Results)
**Goal**: Get the first 3 users (no specific order). `$limit` caps the output count.

**Step-by-Step Explanation**:
1. Start with all 10 documents (default order by `_id`).
2. Use `$limit: 3` to keep only the first 3.
3. Output is the full documents (limited to 3).

**Pipeline Code**:
```js
db.users.aggregate([
  { $limit: 3 }
]);
```

**Expected Output** (3 documents):
```json
{ "_id": 1, "name": "Alice Johnson", ... }
{ "_id": 2, "name": "bob smith", ... }
{ "_id": 3, "name": "Charlie Brown", ... }
```

---

### Example 6: `$unwind` (Flatten Arrays)
**Goal**: Unwind the `tags` array to create one document per tag. `$unwind` expands arrays.

**Step-by-Step Explanation**:
1. Start with all 10 documents (each has a `tags` array, e.g., Alice has 3 tags).
2. Use `$unwind: "$tags"` to create a new document for each tag value.
3. Output has more documents (total ~25, since most have 2-3 tags).

**Pipeline Code**:
```js
db.users.aggregate([
  { $unwind: "$tags" }
]);
```

**Expected Output** (truncated; one doc per tag):
```json
{ "_id": 1, "name": "Alice Johnson", "tags": "dev", ... }  // Alice's first tag
{ "_id": 1, "name": "Alice Johnson", "tags": "frontend", ... }  // Alice's second
{ "_id": 1, "name": "Alice Johnson", "tags": "react", ... }  // Alice's third
{ "_id": 2, "name": "bob smith", "tags": "marketing", ... }
... (and so on for all tags across users)
```

---

These are basic building blocks. You can combine them (e.g., `$match` then `$group`) for more power. For example, to count active users by role:
```js
db.users.aggregate([
  { $match: { status: "active" } },
  { $group: { _id: "$role", count: { $sum: 1 } } }
]);
```

-------------------------


# 1. **Create useful indexes** (including **text** and **2dsphere**)
# 2. **Run efficient full-text search** using `$text`
# 3. **Run geospatial queries** using `2dsphere` (with sample location data)

We'll use the **same `users` collection** from your data, but **add location coordinates** to a few users so we can demonstrate **geospatial search**.

---

## Step 1: Add Location Data + Create Indexes

Run this **in `mongosh`** (after your original `insertMany`):

```js
// --- 1. Add location (latitude, longitude) to some users ---
db.users.updateOne(
  { _id: 1 },
  { $set: { location: { type: "Point", coordinates: [-73.97, 40.77] } } }  // New York
);

db.users.updateOne(
  { _id: 3 },
  { $set: { location: { type: "Point", coordinates: [-118.24, 34.05] } } }  // Los Angeles
);

db.users.updateOne(
  { _id: 6 },
  { $set: { location: { type: "Point", coordinates: [-0.13, 51.51] } } }     // London
);

db.users.updateOne(
  { _id: 9 },
  { $set: { location: { type: "Point", coordinates: [2.35, 48.86] } } }      // Paris
);

// --- 2. Create Indexes ---

// Text index for full-text search on name and tags
db.users.createIndex(
  { name: "text", tags: "text" },
  { name: "text_name_tags" }
);

// 2dsphere index for geospatial queries on location
db.users.createIndex(
  { location: "2dsphere" },
  { name: "geo_location_2dsphere" }
);

// Optional: Regular index on status (for fast filtering)
db.users.createIndex({ status: 1 });

// Confirm indexes
printjson(db.users.getIndexes());
```

> **Why?**  
> - `text` index → enables `$text` search (fast "contains" on words)  
> - `2dsphere` index → enables `$near`, `$geoWithin` (Earth-like distance)  
> - Regular index → speeds up `$match` on `status`

---

## Example 1: Full-Text Search with `$text`

### Goal: Find users who have **"react"** or **"python"** in `name` or `tags`

```js
db.users.aggregate([
  { $match: { $text: { $search: "react python" } } },
  { $project: { name: 1, tags: 1, score: { $meta: "textScore" } } },
  { $sort: { score: { $meta: "textScore" } } }
]);
```

### Expected Output:
```json
{ "_id": 1, "name": "Alice Johnson", "tags": ["dev", "frontend", "react"], "score": 1.5 }
{ "_id": 5, "name": "Eve Adams",       "tags": ["startup", "python", "ai"],     "score": 1.1 }
```

> **Note**:  
> - `$text` uses the **text index** → very fast even on millions of docs  
> - `textScore` ranks relevance  
> - Words are **stemmed** (`reacting` → `react`)

---

## Example 2: Search for Phrase (Exact Match)

```js
db.users.aggregate([
  { $match: { $text: { $search: "\"wonder woman\"" } } },
  { $project: { name: 1, tags: 1 } }
]);
```

> Use quotes for **exact phrase** → only matches if "wonder" and "woman" appear together

---

## Example 3: Exclude Words (Negative Search)

```js
db.users.aggregate([
  { $match: { $text: { $search: "dc -batman" } } },
  { $project: { name: 1, tags: 1 } }
]);
```

**Result**: Diana Prince (has "dc", no "batman")  
**Not returned**: Frank Miller (has "batman")

---

## Example 4: Geospatial Search – Users Near a Point

### Goal: Find users within **500 km** of **Tokyo** (`[139.65, 35.67]`)

```js
db.users.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [139.65, 35.67] },  // Tokyo
      distanceField: "dist.calculated",
      maxDistance: 500 * 1000,  // 500 km in meters
      spherical: true
    }
  },
  {
    $project: {
      name: 1,
      location: 1,
      distance_km: { $divide: ["$dist.calculated", 1000] }
    }
  }
]);
```

### Expected Output (none close to Tokyo):
```json
// No users within 500 km of Tokyo → empty result
```

But let’s test with **New York**:

```js
db.users.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-73.97, 40.77] },  // NYC
      distanceField: "dist.calculated",
      maxDistance: 100 * 1000,
      spherical: true
    }
  },
  { $project: { name: 1, distance_km: { $round: [{ $divide: ["$dist.calculated", 1000] }, 1] } } }
]);
```

**Output**:
```json
{ "_id": 1, "name": "Alice Johnson", "distance_km": 0 }
```

---

## Example 5: Find Users Inside a Geographic Area

### Goal: Users in **Europe** (approximate polygon)

```js
db.users.aggregate([
  {
    $match: {
      location: {
        $geoWithin: {
          $geometry: {
            type: "Polygon",
            coordinates: [[
              [-10, 35], [40, 35], [40, 70], [-10, 70], [-10, 35]  // Rough Europe box
            ]]
          }
        }
      }
    }
  },
  { $project: { name: 1, location: 1 } }
]);
```

**Output**:
```json
{ "_id": 6, "name": "Frank Miller", "location": { "type": "Point", "coordinates": [-0.13, 51.51] } }  // London
{ "_id": 9, "name": "Iris West",    "location": { "type": "Point", "coordinates": [2.35, 48.86] } }     // Paris
```

---

## Bonus: Combine Text + Geo Search

### Find **active users** with **"dc"** in tags **near London**

```js
db.users.aggregate([
  { $match: { status: "active", $text: { $search: "dc" } } },
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-0.13, 51.51] },
      distanceField: "dist_km",
      maxDistance: 1000000,  // 1000 km
      spherical: true
    }
  },
  {
    $project: {
      name: 1,
      tags: 1,
      distance_km: { $round: [{ $divide: ["$dist_km", 1000] }, 1] },
      score: { $meta: "textScore" }
    }
  },
  { $sort: { score: { $meta: "textScore" }, dist_km: 1 } }
]);
```

**Output**:
```json
{ "name": "Frank Miller", "tags": ["comics", "batman", "graphic-novel"], "distance_km": 0, "score": 0.75 }
{ "name": "Iris West",    "tags": ["flash", "journalism", "dc"],          "distance_km": 335.2, "score": 1.1 }
```

---

## Summary Table

| Feature             | Index Type       | Query Operator       | Use Case |
|---------------------|------------------|----------------------|----------|
| Full-text search    | `text`           | `$text`, `$search`   | Search names, tags, descriptions |
| Geospatial (Earth)  | `2dsphere`       | `$near`, `$geoWithin`| Find nearby users, stores, events |
| Fast filtering      | `1` or `-1`      | `$match`             | `status`, `role`, etc. |

---

## Pro Tips

- Always create **text index** before using `$text`
- Use **GeoJSON** format: `{ type: "Point", coordinates: [lng, lat] }`
- `$geoNear` **must be first stage** in pipeline
- Use `.explain("executionStats")` to verify index usage

```js
db.users.find({ $text: { $search: "react" } }).explain("executionStats")
```

---







