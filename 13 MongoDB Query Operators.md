# MongoDB Query Operators

MongoDB provides a variety of query operators that you can use to perform complex queries on your data. Here are some commonly used query operators:

### Comparison Operators:

1. **Equality (`$eq`):**
   - Matches values that are equal to a specified value.

    ```javascript
    { field: { $eq: value } }
    ```

2. **Inequality (`$ne`):**
   - Matches values that are not equal to a specified value.

    ```javascript
    { field: { $ne: value } }
    ```

3. **Greater Than (`$gt`), Less Than (`$lt`), Greater Than or Equal To (`$gte`), Less Than or Equal To (`$lte`):**
   - Matches values based on comparison.

    ```javascript
    { field: { $gt: value } }
    { field: { $lt: value } }
    { field: { $gte: value } }
    { field: { $lte: value } }
    ```

### Logical Operators:

1. **Logical AND (`$and`):**
   - Joins query clauses with a logical AND.

    ```javascript
    { $and: [ { condition1 }, { condition2 } ] }
    ```

2. **Logical OR (`$or`):**
   - Joins query clauses with a logical OR.

    ```javascript
    { $or: [ { condition1 }, { condition2 } ] }
    ```

3. **Logical NOT (`$not`):**
   - Inverts the effect of a query expression.

    ```javascript
    { field: { $not: { $eq: value } } }
    ```

### Element Operators:

1. **Exists (`$exists`):**
   - Matches documents that have the specified field.

    ```javascript
    { field: { $exists: true } }
    ```

2. **Type (`$type`):**
   - Selects documents if a field is of the specified type.

    ```javascript
    { field: { $type: "string" } }
    ```

### Array Operators:

1. **Element Match (`$elemMatch`):**
   - Selects documents if an array field contains at least one element that matches all the specified query criteria.

    ```javascript
    { arrayField: { $elemMatch: { condition1, condition2 } } }
    ```

2. **Size (`$size`):**
   - Matches documents where the array field is a specified size.

    ```javascript
    { arrayField: { $size: size } }
    ```

### Evaluation Operators:

1. **Modulus (`$mod`):**
   - Performs a modulo operation on the value of a field and selects documents with a specified result.

    ```javascript
    { field: { $mod: [ divisor, remainder ] } }
    ```

2. **Type (`$type`):**
   - Selects documents if a field is of the specified BSON data type.

    ```javascript
    { field: { $type: "string" } }
    ```

These are just a few examples of the many query operators available in MongoDB. You can combine and nest these operators to build complex queries that suit your data retrieval needs. For more details, refer to the official documentation: [MongoDB Query and Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/).
