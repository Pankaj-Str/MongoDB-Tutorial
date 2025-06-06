show dbs;
use school;

db.createCollection("student");
show collections;

db.student.insertOne({ name: "joy", age: 30, email: "joy@cwpc.in" });
//db.student.find();

db.student.insertMany([
  { name: "John", age: 25, email: "john@example.com" },
  { name: "Jane", age: 28, email: "jane@example.com" }
]);

//db.student.find();
db.createCollection("products");
db.products.insertMany([
    { name: "Laptop", price: 800, category: "Electronics", stock: 10 },
    { name: "Phone", price: 600, category: "Electronics", stock: 25 },
    { name: "Chair", price: 100, category: "Furniture", stock: 50 }
]);

//db.products.find()

db.products.updateOne(
    { name: "Laptop" }, // Filter
    { $inc: { stock: 5 } } // Update operation
);
//db.products.find();
db.products.updateMany(
    { price: { $gt: 500 } }, // Filter
    { $set: { category: "Premium Electronics" } } // Update operation
);

db.products.find({ price: { $gt: 700 } });


db.createCollection("st");
let students = [];

for (let i = 1; i <= 100; i++) {
    students.push({
        student_id: i,
        name: `Student ${i}`,
        age: Math.floor(Math.random() * 10) + 15,  // age between 15 and 24
        grade: ["A", "B", "C", "D", "F"][Math.floor(Math.random() * 5)],
        subjects: ["Math", "Science", "English", "History", "Art"].slice(0, Math.floor(Math.random() * 5) + 1),
        enrollmentDate: new Date(2023, Math.floor(Math.random() * 12), Math.floor(Math.random() * 28) + 1)
    });
}
db.st.insertMany(students);

db.st.find();
