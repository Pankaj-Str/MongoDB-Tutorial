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
