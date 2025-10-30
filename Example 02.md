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

---

