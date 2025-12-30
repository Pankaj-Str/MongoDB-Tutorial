# MongoDB Aggregation Pipelines

MongoDB Aggregation Pipeline is a powerful framework for data transformation within MongoDB. It allows you to process and transform documents in a collection through a sequence of stages, each representing a specific operation. Aggregation pipelines are typically used for tasks like filtering, sorting, grouping, and performing various transformations on the data.

Here are some common stages used in MongoDB Aggregation Pipelines:

### 1. `$match` Stage:

The `$match` stage filters documents based on specified criteria.

```javascript
db.collection.aggregate([
  { $match: { field: value } }
])
```

### 2. `$project` Stage:

The `$project` stage reshapes documents by specifying which fields to include or exclude.

```javascript
db.collection.aggregate([
  { $project: { newField1: "$oldField1", newField2: 1, _id: 0 } }
])
```

### 3. `$group` Stage:

The `$group` stage groups documents by a specified key and applies aggregate functions.

```javascript
db.collection.aggregate([
  { $group: { _id: "$field", total: { $sum: "$quantity" } } }
])
```

### 4. `$sort` Stage:

The `$sort` stage sorts documents based on specified fields and order.

```javascript
db.collection.aggregate([
  { $sort: { field: 1 } }
])
```

### 5. `$limit` and `$skip` Stages:

The `$limit` stage restricts the number of documents passed to the next stage, and `$skip` skips a specified number of documents.

```javascript
db.collection.aggregate([
  { $limit: 10 },
  { $skip: 5 }
])
```

### 6. `$unwind` Stage:

The `$unwind` stage deconstructs an array field, creating a separate document for each element.

```javascript
db.collection.aggregate([
  { $unwind: "$arrayField" }
])
```

### 7. `$lookup` Stage:

The `$lookup` stage performs a left outer join with another collection.

```javascript
db.orders.aggregate([
  {
    $lookup:
      {
        from: "products",
        localField: "productId",
        foreignField: "_id",
        as: "productDetails"
      }
  }
])
```

### 8. `$facet` Stage:

The `$facet` stage enables the parallel execution of multiple pipelines.

```javascript
db.collection.aggregate([
  {
    $facet: {
      "facet1": [ /* pipeline 1 */ ],
      "facet2": [ /* pipeline 2 */ ]
    }
  }
])
```

These are just a few examples of the many stages available in MongoDB Aggregation Pipelines. You can combine and use these stages to perform complex data transformations and analytics on your MongoDB data. For more details, refer to the official documentation: [MongoDB Aggregation](https://docs.mongodb.com/manual/aggregation/).


### 1. `$group`:

The `$group` stage groups documents by a specified key and allows you to perform aggregate functions on grouped data.

```javascript
db.collection.aggregate([
  { $group: { _id: "$field", count: { $sum: 1 } } }
])
```

### 2. `$limit`:

The `$limit` stage restricts the number of documents passed to the next stage.

```javascript
db.collection.aggregate([
  { $limit: 10 }
])
```

### 3. `$project`:

The `$project` stage reshapes documents by specifying which fields to include or exclude.

```javascript
db.collection.aggregate([
  { $project: { newField1: "$oldField1", newField2: 1, _id: 0 } }
])
```

### 4. `$sort`:

The `$sort` stage sorts documents based on specified fields and order.

```javascript
db.collection.aggregate([
  { $sort: { field: 1 } }
])
```

### 5. `$match`:

The `$match` stage filters documents based on specified criteria.

```javascript
db.collection.aggregate([
  { $match: { field: value } }
])
```

### 6. `$addFields`:

The `$addFields` stage adds new fields to documents or overwrites existing fields.

```javascript
db.collection.aggregate([
  { $addFields: { newField: "value" } }
])
```

### 7. `$count`:

The `$count` stage returns the total number of documents in the aggregation pipeline.

```javascript
db.collection.aggregate([
  { $count: "documentCount" }
])
```

### 8. `$lookup`:

The `$lookup` stage performs a left outer join with another collection.

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "productDetails"
    }
  }
])
```

### 9. `$out`:

The `$out` stage writes the result of the aggregation pipeline to a specified collection.

```javascript
db.collection.aggregate([
  { $out: "newCollection" }
])
```


---- 



### A Step-by-Step Guide 


#### Step 1: Understand What MongoDB Is
MongoDB is a NoSQL database that stores data in flexible, JSON-like documents called BSON (Binary JSON). Unlike traditional relational databases (e.g., SQL), it doesn't use tables with fixed schemas—instead, data is organized into **collections** (like tables) and **documents** (like rows).

- **Why aggregation pipelines?** They let you process, filter, and analyze data directly in the database without pulling everything into your application code. Think of it as a conveyor belt: documents go through a series of "stages" where they're transformed, filtered, grouped, etc.

If you don't have MongoDB installed, proceed to Step 2. Otherwise, skip to Step 3.

#### Step 2: Install and Set Up MongoDB
1. **Download MongoDB Community Edition**: Go to the official website (mongodb.com) and download the free Community Server for your operating system (Windows, macOS, Linux).
   - For Windows/macOS: Use the installer and follow the prompts.
   - For Linux (e.g., Ubuntu): Run commands like `sudo apt update` and `sudo apt install mongodb-org`.

2. **Install MongoDB Shell (mongosh)**: This is the command-line tool for interacting with MongoDB. It comes bundled with the server, or download it separately from mongodb.com.

3. **Start the MongoDB Server**:
   - On Windows/macOS: Run `mongod` in a terminal (it might be in your PATH after installation).
   - On Linux: Use `sudo systemctl start mongod`.
   - By default, it runs on `localhost:27017`.

4. **Open the MongoDB Shell**:
   - In a new terminal, run `mongosh` (or `mongo` in older versions).
   - You'll see a prompt like `test>`. This is where you'll run commands.

5. **Create a Database and Switch to It**:
   - In the shell: `use myDatabase` (this creates/s witches to a database named "myDatabase").

If you encounter issues, refer to the official quickstart guide: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/ (replace with your OS).

#### Step 3: Create a Sample Collection and Insert Data
Before aggregating, we need data. We'll use a simple "sales" collection to track store sales.

1. In the mongosh prompt, create the collection by inserting documents (MongoDB creates it automatically):
   ```javascript
   db.sales.insertMany([
     { item: "apple", qty: 10, price: 1.5, category: "fruit", date: new Date("2023-01-01") },
     { item: "banana", qty: 20, price: 0.5, category: "fruit", date: new Date("2023-02-01") },
     { item: "apple", qty: 5, price: 1.5, category: "fruit", date: new Date("2023-03-01") },
     { item: "carrot", qty: 15, price: 0.8, category: "vegetable", date: new Date("2023-01-15") },
     { item: "banana", qty: 10, price: 0.5, category: "fruit", date: new Date("2023-04-01") },
     { item: "carrot", qty: 25, price: 0.8, category: "vegetable", date: new Date("2023-02-15") },
     { item: "apple", qty: 30, price: 1.5, category: "fruit", date: new Date("2023-05-01") }
   ]);
   ```
   - This inserts 7 documents. Run `db.sales.find().pretty()` to view them.

Now you have a collection ready for aggregation!

#### Step 4: Run Your First Basic Aggregation Pipeline
An aggregation pipeline is an array of stages: `db.collection.aggregate([stage1, stage2, ...])`.

Let's start simple: Find all sales where quantity > 10.

1. Use the `$match` stage to filter:
   ```javascript
   db.sales.aggregate([
     { $match: { qty: { $gt: 10 } } }
   ]).pretty();
   ```
   - **Explanation**: `$match` acts like a WHERE clause in SQL. Here, it filters documents where `qty` is greater than (`$gt`) 10.
   - **Output**: You'll see documents for banana (qty 20), carrot (qty 15 and 25), and apple (qty 30).

#### Step 5: Add Projection to Reshape Data
Now, let's filter and then project only specific fields.

1. Build on the previous pipeline:
   ```javascript
   db.sales.aggregate([
     { $match: { qty: { $gt: 10 } } },
     { $project: { item: 1, qty: 1, totalRevenue: { $multiply: ["$qty", "$price"] }, _id: 0 } }
   ]).pretty();
   ```
   - **Explanation**:
     - `$project` selects fields to include (1) or exclude (0). We include `item` and `qty`, exclude `_id`.
     - We add a new computed field `totalRevenue` using `$multiply` on `qty` and `price`.
   - **Output**: Reshaped documents like `{ "item" : "banana", "qty" : 20, "totalRevenue" : 10 }`.

#### Step 6: Group Data for Summaries
Let's group by `item` and calculate total quantity sold.

1. Add a `$group` stage:
   ```javascript
   db.sales.aggregate([
     { $match: { category: "fruit" } },  // Filter to fruits only
     { $group: { _id: "$item", totalQty: { $sum: "$qty" }, avgPrice: { $avg: "$price" } } }
   ]).pretty();
   ```
   - **Explanation**:
     - `_id: "$item"` groups by the `item` field.
     - `$sum` adds up `qty` for each group.
     - `$avg` computes the average `price`.
   - **Output**: Something like `{ "_id" : "apple", "totalQty" : 45, "avgPrice" : 1.5 }` and similar for banana.

#### Step 7: Sort, Limit, and Skip Results
To organize and paginate:

1. Extend the pipeline:
   ```javascript
   db.sales.aggregate([
     { $match: { category: "fruit" } },
     { $group: { _id: "$item", totalQty: { $sum: "$qty" } } },
     { $sort: { totalQty: -1 } },  // Sort descending by totalQty
     { $limit: 2 },  // Get top 2
     { $skip: 0 }   // Skip none (for pagination example)
   ]).pretty();
   ```
   - **Explanation**:
     - `$sort`: 1 for ascending, -1 for descending.
     - `$limit`: Caps results at 2.
     - `$skip`: Skips the first N (useful for pages, e.g., skip 2 for next page).
   - **Output**: Top-selling fruits, sorted.

#### Step 8: Handle Arrays with Unwind (If Needed)
Suppose we add an array field, like tags: Update one document first:
   ```javascript
   db.sales.updateOne({ item: "apple", qty: 10 }, { $set: { tags: ["red", "sweet", "juicy"] } });
   ```

1. Unwind the array:
   ```javascript
   db.sales.aggregate([
     { $match: { item: "apple" } },
     { $unwind: "$tags" },  // Create one doc per tag element
     { $project: { item: 1, tag: "$tags" } }
   ]).pretty();
   ```
   - **Explanation**: `$unwind` flattens arrays for processing each element separately.

#### Step 9: Join Collections with Lookup
Create a second collection "categories":
   ```javascript
   db.categories.insertMany([
     { _id: "fruit", description: "Edible plant produce" },
     { _id: "vegetable", description: "Edible plant parts" }
   ]);
   ```

1. Join:
   ```javascript
   db.sales.aggregate([
     { $lookup: {
         from: "categories",
         localField: "category",
         foreignField: "_id",
         as: "categoryInfo"
       }
     },
     { $project: { item: 1, category: 1, "categoryInfo.description": 1 } }
   ]).pretty();
   ```
   - **Explanation**: Like a SQL JOIN—matches `category` to `_id` in "categories" and adds as an array `categoryInfo`.

#### Step 10: Advanced: Add Fields, Count, Facet, and Output
1. Add a field:
   ```javascript
   { $addFields: { discountedPrice: { $subtract: ["$price", { $multiply: ["$price", 0.1] }] } } }
   ```

2. Count total documents:
   ```javascript
   db.sales.aggregate([ { $count: "totalSales" } ]);
   ```

3. Facet for multiple views:
   ```javascript
   db.sales.aggregate([
     { $facet: {
         "byCategory": [ { $group: { _id: "$category", count: { $sum: 1 } } } ],
         "highQty": [ { $match: { qty: { $gt: 15 } } }, { $count: "highQtyCount" } ]
       }
     }
   ]).pretty();
   ```
   - Runs sub-pipelines in parallel.

4. Output to a new collection:
   ```javascript
   db.sales.aggregate([
     { $group: { _id: "$item", totalQty: { $sum: "$qty" } } },
     { $out: "itemSummaries" }  // Writes results to new collection
   ]);
   ```
   - View with `db.itemSummaries.find()`.


