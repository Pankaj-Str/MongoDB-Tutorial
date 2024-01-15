# Lesson 2.2: Schemas in MongoDB

In MongoDB, unlike traditional relational databases, there is no strict schema that enforces a specific structure for documents within a collection. MongoDB is a schema-less, document-oriented database, which means each document in a collection can have its own unique structure. However, this doesn't mean that MongoDB doesn't support structure at all.

Here are some points to understand about schemas in MongoDB:

1. **Flexible Schema:**
   - MongoDB allows for dynamic and flexible schemas, enabling documents in the same collection to have different fields.

2. **Field Types:**
   - Documents can contain fields with different data types. For instance, one document can have a field "age" with an integer value, while another document may not have an "age" field at all.

3. **No Predefined Structure:**
   - Unlike traditional relational databases where you define the structure of the table beforehand, MongoDB allows you to insert documents without a predefined schema. Fields can be added or removed as needed.

4. **Dynamic Typing:**
   - MongoDB supports dynamic typing, allowing you to store different data types within the same field across documents.

5. **Schema Validation (Optional):**
   - While MongoDB is schema-less by default, you can enforce a degree of structure using Schema Validation. This allows you to define rules for the structure of documents within a collection. However, this is optional and not always used.

**Example of Schema Validation:**
```javascript
db.createCollection("mycollection", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "age", "city"],
      properties: {
        name: {
          bsonType: "string"
        },
        age: {
          bsonType: "int",
          minimum: 0
        },
        city: {
          bsonType: "string"
        }
      }
    }
  }
})
```

In the above example, we are enforcing that documents in the "mycollection" collection must have the fields "name," "age," and "city," and the "age" field must be of type integer with a minimum value of 0.

Remember that while schema flexibility is one of MongoDB's strengths, it's important to design your schema based on your application's requirements to ensure efficient querying and indexing.