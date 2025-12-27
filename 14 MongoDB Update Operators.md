

# MongoDB Update Operators

Using **MongoDB**

---

## Step 1: Create Database

```js
use companyDB
```

---

## Step 2: Create Dataset (Collection + Documents)

We start with an **employees dataset**.

```js
db.employees.insertMany([
  {
    _id: 1,
    name: "Amit",
    department: "IT",
    salary: 40000,
    experience: 2,
    rating: 3
  },
  {
    _id: 2,
    name: "Neha",
    department: "HR",
    salary: 35000,
    experience: 3,
    rating: 4
  }
])
```

---

## Step 3: View Dataset

```js
db.employees.find()
```

### Output

```js
{
  _id: 1,
  name: "Amit",
  department: "IT",
  salary: 40000,
  experience: 2,
  rating: 3
}
{
  _id: 2,
  name: "Neha",
  department: "HR",
  salary: 35000,
  experience: 3,
  rating: 4
}
```

---

# Applying Update Operators Step by Step

---

## Step 4: `$set` Operator

Used to **update or add new fields**.

### Example: Update department and add location

```js
db.employees.updateOne(
  { _id: 1 },
  { $set: { department: "Data Science", location: "Mumbai" } }
)
```

---

## Step 5: `$unset` Operator

Used to **remove a field**.

### Example: Remove rating field

```js
db.employees.updateOne(
  { _id: 1 },
  { $unset: { rating: 1 } }
)
```

---

## Step 6: `$inc` Operator

Used to **increase or decrease numeric values**.

### Example: Increase salary by 5000

```js
db.employees.updateOne(
  { _id: 1 },
  { $inc: { salary: 5000 } }
)
```

Salary becomes `45000`.

---

## Step 7: `$mul` Operator

Used to **multiply numeric values**.

### Example: Double the experience

```js
db.employees.updateOne(
  { _id: 1 },
  { $mul: { experience: 2 } }
)
```

Experience becomes `4`.

---

## Step 8: `$rename` Operator

Used to **rename a field**.

### Example: Rename `experience` to `totalExperience`

```js
db.employees.updateOne(
  { _id: 1 },
  { $rename: { experience: "totalExperience" } }
)
```

---

## Step 9: `$min` Operator

Updates the field **only if the new value is smaller**.

### Example: Track minimum salary offered

```js
db.employees.updateOne(
  { _id: 1 },
  { $min: { salary: 42000 } }
)
```

Salary becomes `42000` because `42000 < 45000`.

---

## Step 10: `$max` Operator

Updates the field **only if the new value is greater**.

### Example: Track highest salary achieved

```js
db.employees.updateOne(
  { _id: 1 },
  { $max: { salary: 60000 } }
)
```

Salary becomes `60000`.

---

## Step 11: `$currentDate` Operator

Used to **store current date or timestamp**.

### Example: Add last updated timestamp

```js
db.employees.updateOne(
  { _id: 1 },
  { $currentDate: { lastUpdated: true } }
)
```

---

## Step 12: Final Dataset

```js
db.employees.find()
```

### Final Output

```js
{
  _id: 1,
  name: "Amit",
  department: "Data Science",
  salary: 60000,
  totalExperience: 4,
  location: "Mumbai",
  lastUpdated: ISODate("2025-12-27T05:30:00Z")
}
{
  _id: 2,
  name: "Neha",
  department: "HR",
  salary: 35000,
  experience: 3,
  rating: 4
}
```

---

## Operator Summary (Quick Revision)

| Operator       | Use Case                    |
| -------------- | --------------------------- |
| `$set`         | Add or update fields        |
| `$unset`       | Remove fields               |
| `$inc`         | Increase or decrease values |
| `$mul`         | Multiply values             |
| `$rename`      | Rename fields               |
| `$min`         | Store minimum value         |
| `$max`         | Store maximum value         |
| `$currentDate` | Store current date/time     |

---


