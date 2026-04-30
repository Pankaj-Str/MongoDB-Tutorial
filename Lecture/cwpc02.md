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
