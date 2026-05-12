

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
// ===============================================
// Insert 200+ Random Employee Records in MongoDB
// Collection: employees
// ===============================================

db.employees.drop()

const names = [
  "Amit", "Neha", "Rahul", "Priya", "Rohit", "Sneha",
  "Karan", "Pooja", "Vikas", "Anjali", "Suresh", "Meena",
  "Arjun", "Kavita", "Deepak", "Riya", "Manoj", "Nikita",
  "Yash", "Simran", "Aakash", "Komal", "Harsh", "Divya"
]

const departments = [
  "IT",
  "HR",
  "Finance",
  "Marketing",
  "Sales",
  "Support",
  "Admin"
]

let employees = []

for (let i = 1; i <= 250; i++) {

  let employee = {
    _id: i,
    
    name: names[Math.floor(Math.random() * names.length)],

    department: departments[Math.floor(Math.random() * departments.length)],

    salary: Math.floor(Math.random() * 70000) + 30000, 
    // 30000 - 100000

    experience: Math.floor(Math.random() * 15) + 1, 
    // 1 - 15 years

    rating: Math.floor(Math.random() * 5) + 1,
    // 1 - 5 rating

    age: Math.floor(Math.random() * 25) + 22,
    // 22 - 46 age

    city: [
      "Mumbai",
      "Delhi",
      "Pune",
      "Bangalore",
      "Hyderabad",
      "Chennai"
    ][Math.floor(Math.random() * 6)],

    joiningYear: Math.floor(Math.random() * 8) + 2018,

    email: `employee${i}@company.com`,

    active: Math.random() > 0.2
  }

  employees.push(employee)
}

// Insert Records
db.employees.insertMany(employees)

// Check Records
db.employees.find().limit(10)
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


