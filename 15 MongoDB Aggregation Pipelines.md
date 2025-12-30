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

-------

### Simple Beginner Examples of Common MongoDB Aggregation Pipeline Stages

MongoDB has many aggregation stages (also called "commands" or operators starting with `$`). Here are **simple examples** of the most commonly used ones. We'll use the same easy data from before.

#### Sample Data (Run this first)
```javascript
use shop

db.sales.insertMany([
  { item: "apple", quantity: 5, price: 1 },
  { item: "banana", quantity: 8, price: 0.5 },
  { item: "apple", quantity: 7, price: 1 },
  { item: "orange", quantity: 15, price: 2 },
  { item: "banana", quantity: 4, price: 0.5 },
  { item: "apple", quantity: 3, price: 1 },
  { item: "orange", quantity: 10, price: 2 },
  { item: "grape", tags: ["sweet", "purple"], quantity: 20 }
]);
```

#### 1. `$match` - Filter documents (like WHERE in SQL)
```javascript
db.sales.aggregate([
  { $match: { quantity: { $gt: 10 } } }  // Only items with quantity > 10
]).pretty()
```
**Result**: Shows orange (15 and 10) and grape (20).

#### 2. `$project` - Choose or create new fields
```javascript
db.sales.aggregate([
  { $project: { item: 1, totalPrice: { $multiply: ["$quantity", "$price"] }, _id: 0 } }
]).pretty()
```
**Result**: Shows item and calculated totalPrice (e.g., apple: 5).

#### 3. `$group` - Group and calculate (like GROUP BY)
```javascript
db.sales.aggregate([
  { $group: { _id: "$item", totalQty: { $sum: "$quantity" }, avgPrice: { $avg: "$price" } } }
]).pretty()
```
**Result**: One document per item with total quantity and average price.

#### 4. `$sort` - Sort results
```javascript
db.sales.aggregate([
  { $sort: { quantity: -1 } }  // Highest quantity first
]).pretty()
```

#### 5. `$limit` - Show only first N results
```javascript
db.sales.aggregate([
  { $limit: 3 }  // Only top 3 documents
]).pretty()
```

#### 6. `$skip` - Skip first N results (good for pagination)
```javascript
db.sales.aggregate([
  { $skip: 2 },  // Skip first 2
  { $limit: 3 }
]).pretty()
```

#### 7. `$unwind` - Flatten arrays (one document per array item)
```javascript
db.sales.aggregate([
  { $match: { item: "grape" } },
  { $unwind: "$tags" }  // Makes separate document for "sweet" and "purple"
]).pretty()
```

#### 8. `$addFields` - Add a new field (or overwrite)
```javascript
db.sales.aggregate([
  { $addFields: { discount: 0.1 } }  // Adds 10% discount field to every document
]).pretty()
```

#### 9. `$count` - Count total documents after filtering
```javascript
db.sales.aggregate([
  { $match: { quantity: { $gt: 5 } } },
  { $count: "highQuantityItems" }  // Returns { "highQuantityItems": number }
])
```

#### 10. `$lookup` - Join with another collection (like SQL JOIN)
First create another collection:
```javascript
db.categories.insertOne({ _id: "fruit", info: "Healthy and sweet" });
```

Then:
```javascript
db.sales.aggregate([
  { $match: { item: { $in: ["apple", "banana", "orange"] } } },
  { $lookup: { from: "categories", localField: "item", foreignField: "_id", as: "categoryInfo" } }
]).pretty()
```
(Note: This example is simplified; adjust fields for real join.)

#### 11. `$sortByCount` - Group and count, then sort (shortcut)
```javascript
db.sales.aggregate([
  { $sortByCount: "$item" }  // Counts each item and sorts by count descending
]).pretty()
```

#### 12. `$out` - Save results to a new collection
```javascript
db.sales.aggregate([
  { $group: { _id: "$item", total: { $sum: "$quantity" } } },
  { $out: "itemTotals" }  // Creates new collection "itemTotals"
])
```
Check with: `db.itemTotals.find().pretty()`

#### 13. `$facet` - Run multiple pipelines at once
```javascript
db.sales.aggregate([
  { $facet: {
      "topItems": [ { $sortByCount: "$item" }, { $limit: 2 } ],
      "highQty": [ { $match: { quantity: { $gt: 10 } } }, { $count: "count" } ]
    }
  }
]).pretty()
```
**Result**: One document with two fields: topItems and highQty.

These are the most useful stages for beginners. There are more advanced ones (like `$bucket`, `$graphLookup`, `$unionWith`), but start with these!

Practice by changing the data or combining stages. For the full official list, check MongoDB docs: https://www.mongodb.com/docs/manual/reference/operator/aggregation/
