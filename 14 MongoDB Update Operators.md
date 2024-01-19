# MongoDB Update Operators

MongoDB provides update operators that you can use to modify the contents of documents in a collection. Here are some commonly used update operators:

### `$set` Operator:

The `$set` operator updates the value of a field in a document. If the field does not exist, `$set` will create it.

```javascript
db.collection.updateOne({ _id: 1 }, { $set: { key: newValue } })
```

### `$unset` Operator:

The `$unset` operator removes the specified field from a document.

```javascript
db.collection.updateOne({ _id: 1 }, { $unset: { key: 1 } })
```

### `$inc` Operator:

The `$inc` operator increments the value of the specified field by a certain amount.

```javascript
db.collection.updateOne({ _id: 1 }, { $inc: { key: 5 } })
```

### `$mul` Operator:

The `$mul` operator multiplies the value of the specified field by a certain amount.

```javascript
db.collection.updateOne({ _id: 1 }, { $mul: { key: 2 } })
```

### `$rename` Operator:

The `$rename` operator renames a field in a document.

```javascript
db.collection.updateOne({ _id: 1 }, { $rename: { oldKey: "newKey" } })
```

### `$min` and `$max` Operators:

The `$min` operator updates the value of the specified field to a specified value if the specified value is less than the current value.

```javascript
db.collection.updateOne({ _id: 1 }, { $min: { key: minValue } })
```

The `$max` operator updates the value of the specified field to a specified value if the specified value is greater than the current value.

```javascript
db.collection.updateOne({ _id: 1 }, { $max: { key: maxValue } })
```

### `$currentDate` Operator:

The `$currentDate` operator sets the value of a field to the current date or timestamp.

```javascript
db.collection.updateOne({ _id: 1 }, { $currentDate: { key: true } })
```

These are just a few examples of MongoDB update operators. You can use these operators individually or combine them to perform complex updates on your documents. For more details, refer to the official documentation: [MongoDB Update Operators](https://docs.mongodb.com/manual/reference/operator/update/).
