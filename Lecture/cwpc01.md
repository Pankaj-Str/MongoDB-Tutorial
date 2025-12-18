```python

use cwpc;
show dbs;
db.createCollection("School");
show collections;

// insert one item into collections
db.School.insertOne({name:"nishant",age:30,email:"nishant@cwpc.in"})

db.School.insertOne({name:"nishant",age:30,email:"nishant@cwpc.in",height:4.5})


db.School.insertMany([
  {name:"Rohan",age:30,email:"Rohan@cwpc.in"},
  {name:"Niraj",age:30,email:"Niraj@cwpc.in"},
  {name:"Pranali",age:30,email:"Pranali@cwpc.in"},
  {name:"Vijay",age:30,email:"Vijay@cwpc.in"}
  ]);
  
// show records 

db.School.find();


db.School.find().pretty();


db.createCollection("Product");

db.Product.insertMany([
    {name : "Laptop",price:800,category:"Electronics",stock:10},
    {name : "Phone",price:900,category:"Electronics",stock:25},
    {name : "keyboard",price:1600,category:"Electronics",stock:30},
    {name : "Chair",price:4500,category:"Furniture",stock:56},
    {name : "Table",price:600,category:"Furniture",stock:20},
    {name : "USB",price:450,category:"Electronics",stock:60},
    {name : "TV",price:600,category:"Electronics",stock:16},
  ])
  
  
db.Product.find().pretty(); 

db.Product.updateOne(
  {name:"Laptop"},
  {$inc: {stock:5}}
);

db.Product.find().pretty();


db.Product.updateMany(
  {price: {$gt :600}},
  {$set: {category:"Premium Products"}}
  
  )

db.Product.find().pretty();

db.Product.replaceOne(
  {name:"Chair"},
  {Name : "ArmChair",price:7800,category:"Furniture",stock:30}
);


db.Product.find().pretty(); 
  


// Date - 16 -12 -2025

use cwpc;
show dbs;
db.createCollection("School");
show collections;

// insert one item into collections
db.School.insertOne({name:"nishant",age:30,email:"nishant@cwpc.in"})

db.School.insertOne({name:"nishant",age:30,email:"nishant@cwpc.in",height:4.5})


db.School.insertMany([
  {name:"Rohan",age:30,email:"Rohan@cwpc.in"},
  {name:"Niraj",age:30,email:"Niraj@cwpc.in"},
  {name:"Pranali",age:30,email:"Pranali@cwpc.in"},
  {name:"Vijay",age:30,email:"Vijay@cwpc.in"}
  ]);
  
// show records 

db.School.find();


db.School.find().pretty();


db.createCollection("Product");

db.Product.insertMany([
    {name : "Laptop",price:800,category:"Electronics",stock:10},
    {name : "Phone",price:900,category:"Electronics",stock:25},
    {name : "keyboard",price:1600,category:"Electronics",stock:30},
    {name : "Chair",price:4500,category:"Furniture",stock:56},
    {name : "Table",price:600,category:"Furniture",stock:20},
    {name : "USB",price:450,category:"Electronics",stock:60},
    {name : "TV",price:600,category:"Electronics",stock:16},
  ])
  
  
db.Product.find().pretty(); 

db.Product.updateOne(
  {name:"Laptop"},
  {$inc: {stock:5}}
);

db.Product.find().pretty();


db.Product.updateMany(
  {price: {$gt :600}},
  {$set: {category:"Premium Products"}}
  
  )

db.Product.find().pretty();

db.Product.replaceOne(
  {name:"Chair"},
  {Name : "ArmChair",price:7800,category:"Furniture",stock:30}
);


db.Product.find().pretty(); 


// delete data 
db.Product.deleteOne({name: "USB"})


  
db.Product.find().pretty(); 

// create a students Name collections


db.createCollection("student")

db.student.insertMany([
  { name: "Aaron Miller", age: 20, major: "Computer Science", gpa: 3.6, enrolled: true, hobbies: ["coding","gaming"], address: { city: "New York", zip: "10001" }, scores: [88,90,85], graduationYear: 2026, status: "active" },
  { name: "Abigail Johnson", age: 19, major: "Biology", gpa: 3.8, enrolled: true, hobbies: ["reading"], address: { city: "Boston", zip: "02101" }, scores: [92,94,90], graduationYear: 2027, status: "active" },
  { name: "Adam Wilson", age: 22, major: "Economics", gpa: 3.3, enrolled: true, hobbies: ["finance"], address: { city: "Chicago", zip: "60601" }, scores: [84,86,82], graduationYear: 2025, status: "active" },
  { name: "Alexandra Brown", age: 21, major: "Physics", gpa: 3.9, enrolled: true, hobbies: ["astronomy"], address: { city: "Seattle", zip: "98101" }, scores: [95,96,94], graduationYear: 2026, status: "active" },
  { name: "Andrew Davis", age: 23, major: "History", gpa: 3.1, enrolled: false, hobbies: ["writing"], address: { city: "Denver", zip: "80201" }, scores: [78,76,80], graduationYear: null, status: "inactive" },

  { name: "Ashley Martinez", age: 20, major: "Business", gpa: 3.4, enrolled: true, hobbies: ["marketing"], address: { city: "Miami", zip: "33101" }, scores: [86,87,85], graduationYear: 2026, status: "active" },
  { name: "Benjamin Clark", age: 21, major: "Engineering", gpa: 3.7, enrolled: true, hobbies: ["robotics"], address: { city: "San Jose", zip: "95101" }, scores: [90,92,89], graduationYear: 2025, status: "active" },
  { name: "Brianna Lewis", age: 19, major: "Chemistry", gpa: 3.5, enrolled: true, hobbies: ["lab work"], address: { city: "Austin", zip: "73301" }, scores: [88,87,89], graduationYear: 2027, status: "active" },
  { name: "Caleb Walker", age: 22, major: "Math", gpa: 4.0, enrolled: true, hobbies: ["chess"], address: { city: "Madison", zip: "53701" }, scores: [100,99,98], graduationYear: 2025, status: "active" },
  { name: "Catherine Hall", age: 23, major: "Psychology", gpa: 3.6, enrolled: true, hobbies: ["research"], address: { city: "San Diego", zip: "92101" }, scores: [89,90,88], graduationYear: 2024, status: "active" },

  { name: "Daniel Allen", age: 20, major: "Computer Science", gpa: 3.2, enrolled: true, hobbies: ["web dev"], address: { city: "Raleigh", zip: "27601" }, scores: [82,84,80], graduationYear: 2026, status: "probation" },
  { name: "Danielle Young", age: 21, major: "Nursing", gpa: 3.8, enrolled: true, hobbies: ["volunteering"], address: { city: "Columbus", zip: "43004" }, scores: [93,94,92], graduationYear: 2025, status: "active" },
  { name: "David Hernandez", age: 22, major: "Statistics", gpa: 3.5, enrolled: true, hobbies: ["data analysis"], address: { city: "Minneapolis", zip: "55401" }, scores: [88,87,89], graduationYear: 2025, status: "active" },
  { name: "Emily King", age: 19, major: "Art", gpa: 3.9, enrolled: true, hobbies: ["painting","design"], address: { city: "Los Angeles", zip: "90001" }, scores: [96,95,97], graduationYear: 2027, status: "active" },
  { name: "Ethan Wright", age: 24, major: "Law", gpa: 3.0, enrolled: false, hobbies: [], address: { city: "Washington", zip: "20001" }, scores: [], graduationYear: null, status: "inactive" },

  { name: "Hannah Lopez", age: 20, major: "Data Science", gpa: 3.9, enrolled: true, hobbies: ["python","ml"], address: { city: "San Mateo", zip: "94401" }, scores: [97,96,95], graduationYear: 2026, status: "active" },
  { name: "Isaac Thompson", age: 21, major: "Physics", gpa: 3.4, enrolled: true, hobbies: ["gaming"], address: { city: "Phoenix", zip: "85001" }, scores: [85,86,84], graduationYear: 2025, status: "active" },
  { name: "Isabella Moore", age: 22, major: "Business", gpa: 3.6, enrolled: true, hobbies: ["entrepreneurship"], address: { city: "Atlanta", zip: "30301" }, scores: [88,89,90], graduationYear: 2025, status: "active" },
  { name: "Jacob Taylor", age: 23, major: "Engineering", gpa: null, enrolled: true, hobbies: [], address: { city: "Houston" }, scores: [], graduationYear: 2024, status: "probation" },
  { name: "Jasmine Anderson", age: 19, major: "Biology", gpa: 3.7, enrolled: true, hobbies: ["hiking"], address: { city: "Portland", zip: "97201" }, scores: [91,90,92], graduationYear: 2027, status: "active" },

  // ---- remaining records (21–105) ----
  ...Array.from({ length: 85 }, (_, i) => ({
    name: [
      "John Parker","Julia Scott","Kevin Green","Laura Adams","Liam Baker",
      "Madison Nelson","Mark Rivera","Megan Carter","Michael Perez","Natalie Roberts",
      "Nathan Turner","Nicole Phillips","Noah Campbell","Olivia Evans","Owen Edwards",
      "Paige Collins","Rachel Stewart","Ryan Morris","Samantha Rogers","Sean Reed",
      "Sophia Cook","Steven Morgan","Taylor Bell","Thomas Murphy","Victoria Bailey"
    ][i % 25] + ` ${i + 1}`,
    age: 18 + (i % 7),
    major: ["Computer Science","Math","Biology","Engineering","Psychology","Business","Data Science"][i % 7],
    gpa: i % 9 === 0 ? null : Number((3.1 + (i % 8) * 0.1).toFixed(1)),
    enrolled: i % 10 !== 0,
    hobbies: i % 4 === 0 ? [] : ["reading","coding","sports"].slice(0, (i % 3) + 1),
    address: { city: ["NY","Boston","Chicago","Austin","Seattle","LA","Denver"][i % 7] },
    scores: i % 9 === 0 ? [] : [80 + (i % 15), 82 + (i % 12), 85 + (i % 10)],
    graduationYear: i % 10 === 0 ? null : 2024 + (i % 4),
    status: i % 10 === 0 ? "inactive" : i % 8 === 0 ? "probation" : "active"
  }))
]);



// $eq =Equals 

db.student.find({name:{$eq:"Daniel Allen"}}).pretty();

// $ne -> not Equals

db.student.find({major:{$ne:"Computer Science"}}).pretty();

// $gt -> Greter than 

db.student.find({age:{$gt:20}}).pretty();



 
  
  
// $in 
db.student.find({hobbies:{$in: ["coding"]}}).pretty();
db.student.find({hobbies:{$in: ["coding","sports"]}}).pretty();
  
 
// $nin
db.student.find({hobbies:{$nin: ["coding","sports"]}}).pretty();

// $and

db.student.find({$and:[{age:{$gt:21}},{gpa:{$gte:3.5}}]}).pretty();
  
  
 db.student.find({$and:[{age:{$gt:21}},{gpa:{$gte:3.5}}]}).pretty();

// $or

db.student.find({$or:[{age:{$gt:21}},{gpa:{$gte:3.5}}]}).pretty();
  

//$not

db.student.find({age:{$not:{$lt:22}}}).pretty();  

// $nor

db.student.find({$nor:[{major:"Math"},{gpa:4.0}]}).pretty(); 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  



```
