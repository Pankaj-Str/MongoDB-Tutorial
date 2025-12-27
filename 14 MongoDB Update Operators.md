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



---

# Complete Example: `$min` and `$max` in **MongoDB**

### Scenario

You are managing a **student performance system** where:

* You want to store the **highest marks** a student ever scored.
* You want to store the **lowest attendance percentage** recorded.

---

## 1. Create Database and Collection

```js
use schoolDB
```

```js
db.students.insertOne({
  _id: 1,
  name: "Amit",
  highestMarks: 78,
  lowestAttendance: 85
})
```

---

## 2. View Initial Document

```js
db.students.find()
```

### Output

```js
{
  _id: 1,
  name: "Amit",
  highestMarks: 78,
  lowestAttendance: 85
}
```

---

## 3. Update Using `$max` (Highest Marks)

Student scored **82**, which is higher than previous **78**.

```js
db.students.updateOne(
  { _id: 1 },
  { $max: { highestMarks: 82 } }
)
```

Result:

```js
highestMarks becomes 82
```

Updated because `82 > 78`.

---

## 4. Update Using `$max` (Lower Value – No Change)

Student scored **75**.

```js
db.students.updateOne(
  { _id: 1 },
  { $max: { highestMarks: 75 } }
)
```

No update because `75 < 82`.

---

## 5. Update Using `$min` (Lowest Attendance)

Attendance dropped to **80**.

```js
db.students.updateOne(
  { _id: 1 },
  { $min: { lowestAttendance: 80 } }
)
```

Result:

```js
lowestAttendance becomes 80
```

Updated because `80 < 85`.

---

## 6. Update Using `$min` (Higher Value – No Change)

Attendance increased to **90**.

```js
db.students.updateOne(
  { _id: 1 },
  { $min: { lowestAttendance: 90 } }
)
```

No update because `90 > 80`.

---

## 7. `$min` and `$max` Together in One Query

New exam marks and attendance update together.

```js
db.students.updateOne(
  { _id: 1 },
  {
    $max: { highestMarks: 88 },
    $min: { lowestAttendance: 75 }
  }
)
```

---

## 8. Final Document

```js
db.students.find()
```

### Final Output

```js
{
  _id: 1,
  name: "Amit",
  highestMarks: 88,
  lowestAttendance: 75
}
```

---




