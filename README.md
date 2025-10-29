

## MongoDB Command List (mongosh)  
*(Run inside `mongosh` unless specified)*

---

### 1. **Basic Connection & Shell Commands**
| Command | Description |
|--------|-----------|
| `mongosh` | Start MongoDB shell |
| `mongosh --host <host> --port <port>` | Connect to specific host/port |
| `mongosh "mongodb://user:pass@localhost:27017/db"` | Connect with auth |
| `exit` or `Ctrl+C` | Exit shell |
| `cls` | Clear screen |
| `db.version()` | Show MongoDB server version |
| `db.stats()` | Current database stats |
| `db.hostInfo()` | Host system info |
| `db.serverStatus()` | Server status metrics |

---

### 2. **Database Commands**
| Command | Description |
|--------|-----------|
| `use <db_name>` | Switch to or create database |
| `show dbs` | List all databases |
| `show databases` | Same as `show dbs` |
| `db` | Show current database |
| `db.dropDatabase()` | Delete current database |
| `db.createCollection("name")` | Explicitly create collection |
| `db.getCollectionNames()` | List collections in current DB |
| `show collections` | List collections |
| `db.getCollection("coll")` | Get collection reference |
| `db.stats()` | Database stats (size, collections, etc.) |

---

### 3. **Collection Commands**
| Command | Description |
|--------|-----------|
| `db.createCollection("students", { capped: true, size: 100000 })` | Create capped collection |
| `db.<coll>.drop()` | Drop collection |
| `db.<coll>.renameCollection("newname")` | Rename collection |
| `db.<coll>.stats()` | Collection stats |
| `db.<coll>.storageSize()` | Storage size in bytes |
| `db.<coll>.totalSize()` | Total size (data + indexes) |
| `db.<coll>.dataSize()` | Data size only |
| `db.<coll>.countDocuments({})` | Count documents (accurate) |
| `db.<coll>.estimatedDocumentCount()` | Fast approximate count |
| `db.<coll>.find().count()` | **Deprecated** — avoid |

---

### 4. **Insert Commands**
| Command | Description |
|--------|-----------|
| `db.<coll>.insertOne({ doc })` | Insert one document |
| `db.<coll>.insertMany([doc1, doc2])` | Insert multiple |
| `db.<coll>.insert({ doc })` | **Legacy** — works but not recommended |

> Returns: `_id` of inserted document(s)

---

### 5. **Query & Read Commands**
| Command | Description |
|--------|-----------|
| `db.<coll>.find()` | Find all documents |
| `db.<coll>.find().pretty()` | Formatted output |
| `db.<coll>.findOne()` | Return first matching document |
| `db.<coll>.find({ field: value })` | Query with filter |
| `db.<coll>.find({ age: { $gt: 18 } })` | Comparison query |

#### **Projection**
```javascript
db.coll.find({}, { name: 1, _id: 0 })  // Include name, exclude _id
```

#### **Sorting**
```javascript
db.coll.find().sort({ age: -1 })     // Descending
db.coll.find().sort({ name: 1 })     // Ascending
```

#### **Limit & Skip**
```javascript
db.coll.find().limit(10)
db.coll.find().skip(5)
```

#### **Cursor Methods**
| Method | Description |
|-------|-----------|
| `.forEach(doc => printjson(doc))` | Iterate results |
| `.toArray()` | Convert cursor to array |
| `.hasNext()` / `.next()` | Manual cursor control |

---

### 6. **Update Commands**
| Command | Description |
|--------|-----------|
| `db.<coll>.updateOne(filter, update, options)` | Update first match |
| `db.<coll>.updateMany(filter, update)` | Update all matches |
| `db.<coll>.replaceOne(filter, replacement)` | Replace entire doc |

#### **Update Operators**
| Operator | Use |
|--------|-----|
| `$set` | Set field value |
| `$unset` | Remove field |
| `$inc` | Increment number |
| `$mul` | Multiply number |
| `$rename` | Rename field |
| `$push` | Add to array |
| `$pop` | Remove from array end |
| `$pull` | Remove by value |
| `$addToSet` | Add if not exists |
| `$currentDate` | Set to current time |

**Example:**
```javascript
db.students.updateOne(
  { name: "Ami" },
  { $set: { age: 18 }, $push: { hobbies: "Coding" } }
)
```

> Use `{ upsert: true }` to insert if not found

---

### 7. **Delete Commands**
| Command | Description |
|--------|-----------|
| `db.<coll>.deleteOne(filter)` | Delete first match |
| `db.<coll>.deleteMany(filter)` | Delete all matches |
| `db.<coll>.remove(filter, { justOne: true })` | **Legacy** |

---

### 8. **Aggregation Framework**
| Stage | Command |
|------|--------|
| `$match` | Filter documents |
| `$project` | Reshape (include/exclude/rename) |
| `$group` | Group by field |
| `$sort` | Sort results |
| `$limit` / `$skip` | Pagination |
| `$unwind` | Deconstruct array |
| `$lookup` | Join with another collection |
| `$addFields` | Add computed fields |
| `$count` | Count documents |
| `$out` / `$merge` | Write output |

**Example:**
```javascript
db.sales.aggregate([
  { $match: { status: "A" } },
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } },
  { $limit: 5 }
])
```

---

### 9. **Indexing Commands**
| Command | Description |
|--------|-----------|
| `db.<coll>.createIndex({ field: 1 })` | Ascending index |
| `db.<coll>.createIndex({ field: -1 })` | Descending |
| `db.<coll>.createIndex({ a: 1, b: 1 })` | Compound |
| `db.<coll>.createIndex({ loc: "2dsphere" })` | Geospatial |
| `db.<coll>.createIndex({ text: "text" })` | Text index |
| `db.<coll>.createIndex({ field: 1 }, { unique: true })` | Unique |
| `db.<coll>.createIndex({ field: 1 }, { name: "idx_name" })` | Named index |

#### **Index Management**
| Command | Description |
|--------|-----------|
| `db.<coll>.getIndexes()` | List all indexes |
| `db.<coll>.dropIndex("index_name")` | Drop by name |
| `db.<coll>.dropIndexes()` | Drop all non-_id indexes |
| `db.<coll>.totalIndexSize()` | Total index size |

---

### 10. **Admin & System Commands**
| Command | Description |
|--------|-----------|
| `db.runCommand({ ping: 1 })` | Test connection |
| `db.runCommand({ buildInfo: 1 })` | Build info |
| `db.runCommand({ collStats: "coll" })` | Collection stats |
| `db.runCommand({ dbStats: 1 })` | DB stats |
| `db.runCommand({ serverStatus: 1 })` | Server metrics |
| `db.runCommand({ listDatabases: 1 })` | List all DBs |
| `db.runCommand({ listCollections: 1 })` | List collections |
| `db.adminCommand(...)` | Run on admin DB |

---

### 11. **User & Authentication**
| Command | Description |
|--------|-----------|
| `use admin` | Switch to admin DB |
| `db.createUser({ user: "admin", pwd: "pass", roles: ["root"] })` | Create user |
| `db.updateUser("user", { pwd: "newpass" })` | Change password |
| `db.dropUser("user")` | Delete user |
| `db.auth("user", "pass")` | Authenticate in shell |
| `db.getUsers()` | List users |
| `db.changeUserPassword("user", "new")` | Change password |

---

### 12. **Replication Commands**
| Command | Description |
|--------|-----------|
| `rs.status()` | Replica set status |
| `rs.initiate()` | Initialize replica set |
| `rs.conf()` | Configuration |
| `rs.add("host:port")` | Add member |
| `rs.remove("host")` | Remove member |
| `rs.stepDown()` | Step down primary |
| `rs.reconfig(cfg)` | Reconfigure |
| `rs.isMaster()` | Check if primary |

---

### 13. **Sharding Commands**
| Command | Description |
|--------|-----------|
| `sh.enableSharding("db")` | Enable sharding on DB |
| `sh.shardCollection("db.coll", { key: 1 })` | Shard collection |
| `sh.status()` | Sharding status |
| `sh.addShard("host")` | Add shard |
| `sh.moveChunk(...)` | Move chunk |
| `sh.splitAt("db.coll", { key: value })` | Split chunk |

---

### 14. **Backup & Restore (mongosh + CLI)**
| CLI Command | Description |
|-----------|-----------|
| `mongodump --db dbname` | Backup database |
| `mongorestore --db dbname dump/dbname` | Restore |
| `mongoexport --db db --collection coll --out file.json` | Export to JSON |
| `mongoimport --db db --collection coll --file file.json` | Import |

---

### 15. **Data Types & Special Values**
| Type | Example |
|------|--------|
| String | `"Pava"` |
| Number | `17`, `7.50` |
| Boolean | `true` |
| Null | `null` |
| Array | `["Games", "Code"]` |
| Object | `{ name: "Ami" }` |
| ObjectId | `ObjectId("671a...")` |
| Date | `ISODate("2025-10-29")` |
| Regex | `/^A/` |
| Binary | `BinData(0, "abc=")` |

---

### 16. **Query & Projection Operators (Full List)**

#### **Comparison**
| Operator | Meaning |
|--------|--------|
| `$eq` | Equals |
| `$ne` | Not equals |
| `$gt` | Greater than |
| `$gte` | Greater than or equal |
| `$lt` | Less than |
| `$lte` | Less than or equal |
| `$in` | In array |
| `$nin` | Not in array |

#### **Logical**
| Operator | Meaning |
|--------|--------|
| `$and` | All true |
| `$or` | Any true |
| `$not` | Negate |
| `$nor` | None true |

#### **Element**
| Operator | Meaning |
|--------|--------|
| `$exists` | Field exists |
| `$type` | Field type |

#### **Array**
| Operator | Meaning |
|--------|--------|
| `$all` | Contains all |
| `$elemMatch` | Match element in array |
| `$size` | Array length |

#### **Evaluation**
| Operator | Meaning |
|--------|--------|
| `$mod` | Modulo |
| `$regex` | Regex match |
| `$text` | Text search (with index) |

---

### 17. **Cursor & Output Control**
| Command | Description |
|--------|-----------|
| `DBQuery.shellBatchSize = 50` | Set batch size |
| `it` | Show next batch (after cursor) |
| `printjson(doc)` | Print formatted |
| `cursor.explain("executionStats")` | Query plan |

---

### 18. **Transactions (Multi-Document)**
```javascript
const session = db.getMongo().startSession();
session.startTransaction();
try {
  db.coll1.insertOne({ x: 1 }, { session });
  db.coll2.updateOne({}, { $inc: { y: 1 } }, { session });
  session.commitTransaction();
} catch (e) {
  session.abortTransaction();
}
session.endSession();
```

---

## Summary: All Commands Cheat Sheet

```javascript
// Core
use db, show dbs, db.dropDatabase()
db.createCollection(), show collections

// CRUD
insertOne(), insertMany()
find(), findOne(), pretty()
updateOne(), updateMany(), replaceOne()
deleteOne(), deleteMany()

// Aggregation
aggregate([ { $match }, { $group }, ... ])

// Index
createIndex(), getIndexes(), dropIndex()

// Admin
db.runCommand({ ping: 1 }), serverStatus()

// Replica Set
rs.status(), rs.initiate()

// Sharding
sh.enableSharding(), sh.shardCollection()

// Auth
db.createUser(), db.auth()
```

---

