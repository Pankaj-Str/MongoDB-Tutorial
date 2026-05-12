```yml
// show database
show dbs;
// create database
use company;
// create collections
db.createCollection("employee_info");

db.createCollection("students_info");

show collections;
// insert data at one 
db.employee_info.insertOne({name:"joy",age:78,email:"joy@cwpc.in"});

// insert multiple data 
db.employee_info.insertMany([
  {name:'raj',age:34,height:5.6,salary:56000},
  {name:'shubham',age:23,height:4.6,salary:56000,dept:"IT"},
  {name:'Khushboo',age:17,height:4.6,salary:78000,city:"mumbai"}
  ]);
  
// show record ...
db.employee_info.find();

```
### 2 May 2026

```yml

db.students.insertMany([
  {
    name: "Alice",
    age: 20,
    major: "Computer Science",
    gpa: 3.8,
    graduationYear: 2024,
    address: { city: "New York", zip: "10001" },
    status: "active",
    hobbies: ["Reading", "Coding"]
  },
  {
    name: "Bob",
    age: 22,
    major: "Biology",
    gpa: 3.5,
    graduationYear: 2023,
    address: { city: "Boston", zip: "02101" },
    status: "inactive",
    hobbies: ["Sports"]
  },
  {
    name: "Charlie",
    age: 19,
    major: "Math",
    gpa: 4,
    address: { city: "Chicago" },
    status: "active",
    hobbies: ["Music"]
  },
  {
    name: "Diana",
    age: 21,
    major: "Physics",
    gpa: 3.9,
    graduationYear: 2025,
    address: { city: "LA", zip: "90001" },
    status: "active",
    hobbies: ["Gaming", "Reading"]
  },
  {
    name: "Eve",
    age: 23,
    major: "Computer Science",
    gpa: null,
    graduationYear: 2026,
    address: { city: "Seattle", zip: "98101" },
    status: "probation"
  }
])

db.students.insertMany([
  { name: "Aaron", age: 18, major: "Computer Science", gpa: 3.1, graduationYear: 2027, address: { city: "San Diego", zip: "92101" }, status: "active", hobbies: ["Coding"] },
  { name: "Bella", age: 21, major: "Math", gpa: 3.6, graduationYear: 2025, address: { city: "Columbus", zip: "43004" }, status: "active", hobbies: ["Reading"] },
  { name: "Caleb", age: 22, major: "Physics", gpa: 2.8, graduationYear: 2024, address: { city: "Charlotte", zip: "28201" }, status: "probation", hobbies: ["Gaming"] },
  { name: "Delilah", age: 20, major: "Biology", gpa: 3.9, graduationYear: 2026, address: { city: "Detroit", zip: "48201" }, status: "active", hobbies: ["Music"] },
  { name: "Ethan", age: 23, major: "Economics", gpa: 3.2, graduationYear: 2023, address: { city: "Memphis", zip: "37501" }, status: "inactive", hobbies: ["Sports"] },
  { name: "Fiona", age: 19, major: "Chemistry", gpa: 3.7, graduationYear: 2027, address: { city: "Baltimore", zip: "21201" }, status: "active", hobbies: ["Reading", "Travel"] },
  { name: "George", age: 24, major: "Computer Science", gpa: 3.4, graduationYear: 2023, address: { city: "Nashville", zip: "37011" }, status: "active", hobbies: ["Chess"] },
  { name: "Hannah", age: 22, major: "Physics", gpa: 3.8, graduationYear: 2024, address: { city: "Louisville", zip: "40201" }, status: "active", hobbies: ["Music", "Coding"] },
  { name: "Isaac", age: 20, major: "Math", gpa: 2.9, graduationYear: 2026, address: { city: "Milwaukee", zip: "53201" }, status: "probation", hobbies: ["Gaming"] },
  { name: "Julia", age: 21, major: "Biology", gpa: 3.5, graduationYear: 2025, address: { city: "Albuquerque", zip: "87101" }, status: "active", hobbies: ["Travel"] },

  { name: "Kevin", age: 23, major: "Chemistry", gpa: 3.0, graduationYear: 2024, address: { city: "Tucson", zip: "85701" }, status: "inactive", hobbies: ["Sports"] },
  { name: "Lily", age: 19, major: "Economics", gpa: 3.9, graduationYear: 2027, address: { city: "Fresno", zip: "93650" }, status: "active", hobbies: ["Reading"] },
  { name: "Mason", age: 22, major: "Computer Science", gpa: 3.3, graduationYear: 2025, address: { city: "Sacramento", zip: "94203" }, status: "active", hobbies: ["Coding", "Gaming"] },
  { name: "Nora", age: 20, major: "Math", gpa: 3.4, graduationYear: 2026, address: { city: "Kansas City", zip: "64101" }, status: "active", hobbies: ["Music"] },
  { name: "Owen", age: 24, major: "Physics", gpa: 2.7, graduationYear: 2023, address: { city: "Mesa", zip: "85201" }, status: "probation", hobbies: ["Sports"] },
  { name: "Paula", age: 21, major: "Biology", gpa: 3.6, graduationYear: 2025, address: { city: "Omaha", zip: "68101" }, status: "active", hobbies: ["Travel"] },
  { name: "Quentin", age: 22, major: "Chemistry", gpa: 3.5, graduationYear: 2024, address: { city: "Raleigh", zip: "27601" }, status: "active", hobbies: ["Reading"] },
  { name: "Rachel", age: 19, major: "Computer Science", gpa: 3.8, graduationYear: 2027, address: { city: "Miami", zip: "33101" }, status: "active", hobbies: ["Coding"] },
  { name: "Samuel", age: 23, major: "Economics", gpa: 3.2, graduationYear: 2023, address: { city: "Cleveland", zip: "44101" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Tina", age: 20, major: "Math", gpa: 3.7, graduationYear: 2026, address: { city: "Virginia Beach", zip: "23450" }, status: "active", hobbies: ["Music"] },

  { name: "Uma", age: 21, major: "Physics", gpa: 3.1, graduationYear: 2025, address: { city: "Oakland", zip: "94601" }, status: "active", hobbies: ["Travel"] },
  { name: "Victor", age: 22, major: "Biology", gpa: 2.9, graduationYear: 2024, address: { city: "Minneapolis", zip: "55401" }, status: "probation", hobbies: ["Sports"] },
  { name: "Wendy", age: 19, major: "Chemistry", gpa: 3.6, graduationYear: 2027, address: { city: "Tulsa", zip: "74101" }, status: "active", hobbies: ["Reading"] },
  { name: "Xavier", age: 23, major: "Computer Science", gpa: 3.4, graduationYear: 2023, address: { city: "Arlington", zip: "76001" }, status: "active", hobbies: ["Coding"] },
  { name: "Yara", age: 20, major: "Economics", gpa: 3.5, graduationYear: 2026, address: { city: "New Orleans", zip: "70112" }, status: "active", hobbies: ["Music"] },
  { name: "Zane", age: 24, major: "Math", gpa: 3.0, graduationYear: 2023, address: { city: "Wichita", zip: "67201" }, status: "inactive", hobbies: ["Gaming"] },

  { name: "Aisha", age: 21, major: "Biology", gpa: 3.7, graduationYear: 2025, address: { city: "Bakersfield", zip: "93301" }, status: "active", hobbies: ["Travel"] },
  { name: "Brandon", age: 22, major: "Physics", gpa: 3.2, graduationYear: 2024, address: { city: "Tampa", zip: "33601" }, status: "active", hobbies: ["Sports"] },
  { name: "Catherine", age: 20, major: "Chemistry", gpa: 3.9, graduationYear: 2026, address: { city: "Aurora", zip: "80010" }, status: "active", hobbies: ["Reading"] },
  { name: "Derek", age: 23, major: "Computer Science", gpa: 3.3, graduationYear: 2023, address: { city: "Anaheim", zip: "92801" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Elena", age: 19, major: "Math", gpa: 3.8, graduationYear: 2027, address: { city: "Honolulu", zip: "96801" }, status: "active", hobbies: ["Music"] },

  { name: "Farhan", age: 22, major: "Economics", gpa: 3.4, graduationYear: 2024, address: { city: "Santa Ana", zip: "92701" }, status: "active", hobbies: ["Travel"] },
  { name: "Gabriella", age: 21, major: "Physics", gpa: 3.6, graduationYear: 2025, address: { city: "Riverside", zip: "92501" }, status: "active", hobbies: ["Reading"] },
  { name: "Harold", age: 24, major: "Chemistry", gpa: 2.8, graduationYear: 2023, address: { city: "Corpus Christi", zip: "78401" }, status: "probation", hobbies: ["Sports"] },
  { name: "Isabella", age: 20, major: "Biology", gpa: 3.9, graduationYear: 2026, address: { city: "Lexington", zip: "40507" }, status: "active", hobbies: ["Music"] },
  { name: "Jonah", age: 23, major: "Computer Science", gpa: 3.5, graduationYear: 2023, address: { city: "Stockton", zip: "95201" }, status: "active", hobbies: ["Coding"] },

  { name: "Kylie", age: 19, major: "Math", gpa: 3.6, graduationYear: 2027, address: { city: "Henderson", zip: "89002" }, status: "active", hobbies: ["Reading"] },
  { name: "Landon", age: 22, major: "Economics", gpa: 3.1, graduationYear: 2024, address: { city: "Saint Paul", zip: "55101" }, status: "inactive", hobbies: ["Gaming"] },
  { name: "Monica", age: 21, major: "Physics", gpa: 3.7, graduationYear: 2025, address: { city: "St. Louis", zip: "63101" }, status: "active", hobbies: ["Travel"] },
  { name: "Noah", age: 20, major: "Chemistry", gpa: 3.4, graduationYear: 2026, address: { city: "Cincinnati", zip: "45201" }, status: "active", hobbies: ["Sports"] },
  { name: "Olga", age: 24, major: "Biology", gpa: 3.2, graduationYear: 2023, address: { city: "Pittsburgh", zip: "15201" }, status: "inactive", hobbies: ["Music"] },

  { name: "Peter", age: 23, major: "Computer Science", gpa: 3.8, graduationYear: 2024, address: { city: "Greensboro", zip: "27401" }, status: "active", hobbies: ["Coding"] },
  { name: "Queenie", age: 19, major: "Math", gpa: 3.5, graduationYear: 2027, address: { city: "Anchorage", zip: "99501" }, status: "active", hobbies: ["Reading"] },
  { name: "Rohan", age: 21, major: "Physics", gpa: 3.3, graduationYear: 2025, address: { city: "Plano", zip: "75023" }, status: "active", hobbies: ["Gaming"] },
  { name: "Sophia", age: 22, major: "Economics", gpa: 3.9, graduationYear: 2024, address: { city: "Lincoln", zip: "68501" }, status: "active", hobbies: ["Travel"] },
  { name: "Thomas", age: 24, major: "Chemistry", gpa: 2.9, graduationYear: 2023, address: { city: "Orlando", zip: "32801" }, status: "probation", hobbies: ["Sports"] }
]);


// db.students.find() // show all record 
// db.students.find({major:"Economics"});
// db.students.find({age :{ $gt:22 }});
// db.students.find({age :{ $lt:22 }});
// db.students.find({ graduationYear : 2026 , age: {$lt : 22} });
// db.students.find({age:{ $eq : 20} });
//db.students.find({age:{ $ne : 20} });
//db.students.find({
//  $or:[
//      {age: {$gt: 20}},
//      {gpa: {$lt:3.0}}
//    ]
//});

// db.students.find({
//   $and:[
//       {age: {$gt: 22}},
//       {gpa: {$lt:3.0}}
//     ]
  
// });

// db.students.find({hobbies : {$in: ['Coding','Music']}});
// db.students.find().sort({ age: 1 });

```
- $eq: Equal to a value.
- $ne: Not equal to a value.
- $gt: Greater than a value.
- $gte: Greater than or equal to a value.
- $lt: Less than a value.
- $lte: Less than or equal to a value.
- $in: Matches any value in an array.
- $or: Combines multiple conditions with OR logic.
- $and: Combines multiple conditions with AND logic.

### Date : 5 May 2026

```xml

// limit and skip

// db.students.find().sort({
//   name: -1
// }).limit(3).skip(3);


// update 
db.students.updateOne(
    { name:"Alice" },
    { $set : { age: 21 }, $push : { hobbies : "Swimming" }}
    
)

db.students.find( {name: "Alice" });

// update many 
db.students.updateMany(
  
  { status : "active" },
  { $inc : { gpa : 0.1 }}
)


db.students.find( {name: "Alice" });

// replaceOne 

db.students.replaceOne(
    { name : "Alice" },
    { name : "Alice" ,age: 34 , major: "Design ", gpa : 3.7 }
);


db.students.find( {name: "Alice" });

// delete 
db.students.deleteOne( { name: "Alice" } );

// deleteMany
db.students.deleteMany( { status: "active" } );

db.students.find();

```
## Date 12 May 2026

```yml



// Operator	Use Case
// $set	Add or update fields
// $unset	Remove fields
// $inc	Increase or decrease values
// $mul	Multiply values
// $rename	Rename fields
// $min	Store minimum value
// $max	Store maximum value
// $currentDate	Store current date/time





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
  },
  {
    _id: 3,
    name: "Rahul",
    department: "Finance",
    salary: 50000,
    experience: 5,
    rating: 5
  },
  {
    _id: 4,
    name: "Priya",
    department: "Sales",
    salary: 32000,
    experience: 1,
    rating: 2
  },
  {
    _id: 5,
    name: "Karan",
    department: "IT",
    salary: 60000,
    experience: 7,
    rating: 5
  }
])


// Insert 200+ Employees Automatically
let departments = ["IT", "HR", "Finance", "Sales", "Marketing"];
let names = [
  "Amit", "Neha", "Rahul", "Priya", "Karan",
  "Sneha", "Rohit", "Anjali", "Vikas", "Pooja"
];

let employees = [];

for (let i = 1; i <= 200; i++) {
  employees.push({
    _id: i,
    name: names[Math.floor(Math.random() * names.length)] + i,
    department: departments[Math.floor(Math.random() * departments.length)],
    salary: Math.floor(Math.random() * 50000) + 30000,
    experience: Math.floor(Math.random() * 10) + 1,
    rating: Math.floor(Math.random() * 5) + 1
  });
}

db.employees.insertMany(employees);

// Check Records
// db.employees.find().limit(10)

// $set - update operator 
db.employees.updateOne(
  { _id: 1 },
  { $set: { department: "Sales", location: "Surat" } }
);



// $unset() - remove

db.employees.updateOne(
  { _id: 1 },
  { $unset: { rating: 1 } }
);



// $inc()
db.employees.updateOne(
  { _id: 1 },
  { $inc: { salary: 5000 } }
);


db.employees.find({_id:1});

// $mul()

db.employees.updateOne(
  { _id: 1 },
  { $mul: { experience: 2 } }
)

db.employees.find({_id:1});

// $rename 
db.employees.updateOne(
  { _id: 1 },
  { $rename: { experience: "totalExperience" } }
);

db.employees.find({_id:1});

// $min -> Salary becomes 42000 because 42000 < 45000.

db.employees.updateOne(
  { _id: 1 },
  { $min: { salary: 42000 } }
);

db.employees.find({_id:1});


// $max

db.employees.updateOne(
  { _id: 1 },
  { $max: { salary: 60000 } }
)


db.employees.find({_id:1});

// $currentDate

db.employees.updateOne(
  { _id: 1 },
  { $currentDate: { lastUpdated: true } }
)


db.employees.find({_id:1});

```
