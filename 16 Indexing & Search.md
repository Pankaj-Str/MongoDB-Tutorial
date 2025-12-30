### Beginner-Level Step-by-Step Example: MongoDB Indexing and Search


We'll use the MongoDB shell (`mongosh`). Assume you have MongoDB installed (local or Atlas free tier). If not, see previous guides for setup.

#### Step 1: Set Up Sample Data
We'll use a "books" collection with simple documents including titles, authors, and descriptions.

Run these in `mongosh`:

```javascript
use library  // Switch to/create 'library' database

db.books.insertMany([
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 1925, genre: "Fiction", description: "A story of wealth and tragedy in the Jazz Age." },
  { title: "To Kill a Mockingbird", author: "Harper Lee", year: 1960, genre: "Fiction", description: "A novel about racism and innocence in the American South." },
  { title: "1984", author: "George Orwell", year: 1949, genre: "Dystopian", description: "A tale of totalitarianism and surveillance in a future society." },
  { title: "Pride and Prejudice", author: "Jane Austen", year: 1813, genre: "Romance", description: "A romantic comedy about manners and marriage." },
  { title: "The Catcher in the Rye", author: "J.D. Salinger", year: 1951, genre: "Fiction", description: "A young boy's rebellion against phony adult world." }
]);
```

View the data (optional):
```javascript
db.books.find().pretty()
```

#### Step 2: Understand and Create a Basic Index
Without indexes, MongoDB scans every document for queries (slow for large collections). Indexes store sorted values for quick lookups.

1. Check existing indexes (MongoDB auto-creates one on `_id`):
   ```javascript
   db.books.getIndexes()
   ```
   - Output: Shows the default `_id` index.

2. Create a simple index on the `year` field (for faster queries by year):
   ```javascript
   db.books.createIndex({ year: 1 })  // 1 = ascending order
   ```
   - **Explanation**: This indexes the `year` field. Now queries like `find({ year: 1925 })` are faster.

3. Test a query without/with index (explain to see difference):
   ```javascript
   db.books.explain("executionStats").find({ year: { $gt: 1900 } })
   ```
   - Before index: Might show "COLLSCAN" (full scan).
   - After: Shows "IXSCAN" (uses index, faster).

#### Step 3: Create Compound and Unique Indexes
- **Compound Index**: Indexes multiple fields together.
  ```javascript
  db.books.createIndex({ author: 1, year: -1 })  // Ascending author, descending year
  ```
  - Useful for queries like `find({ author: "Harper Lee", year: { $lt: 2000 } })`.

- **Unique Index**: Ensures no duplicates.
  ```javascript
  db.books.createIndex({ title: 1 }, { unique: true })
  ```
  - Now inserting a duplicate title fails.

Drop an index if needed:
```javascript
db.books.dropIndex({ year: 1 })
```

#### Step 4: Set Up MongoDB Atlas Search (For Full-Text Search)
MongoDB's built-in text search is basic; for advanced (fuzzy, relevance), use **Atlas Search** (free on Atlas cloud).

1. **Sign up for MongoDB Atlas** (if not done): Go to mongodb.com/atlas, create a free cluster.

2. In Atlas UI:
   - Go to your cluster > "Search" tab > Create Search Index.
   - Name: "default" (or custom).
   - Use JSON editor for config:
     ```json
     {
       "mappings": {
         "dynamic": true  // Auto-index all fields
       }
     }
     ```
   - This indexes all fields for search.

3. Back in `mongosh` (connect to Atlas via connection string from UI).

#### Step 5: Perform a Basic Text Search
Using `$text` operator (built-in, no Atlas needed for simple cases).

1. First, create a text index on `description` and `title`:
   ```javascript
   db.books.createIndex({ title: "text", description: "text" })
   ```

2. Search for words like "society" or "romantic":
   ```javascript
   db.books.find({ $text: { $search: "society romantic" } }).pretty()
   ```
   - **Explanation**: Matches documents with "society" OR "romantic". Results include relevance score.
   - Output: Might return "1984" and "Pride and Prejudice".

#### Step 6: Advanced Search with Atlas Search
(Requires Atlas setup from Step 4).

Use `$search` stage in aggregation for powerful queries.

1. Simple fuzzy search for "totalitarianizm" (misspelled):
   ```javascript
   db.books.aggregate([
     {
       $search: {
         index: "default",  // Your index name
         text: {
           query: "totalitarianizm",
           path: ["title", "description"],  // Fields to search
           fuzzy: { maxEdits: 2 }  // Allow 2 letter edits (fuzzy matching)
         }
       }
     },
     { $project: { title: 1, description: 1, score: { $meta: "searchScore" } } }
   ]).pretty()
   ```
   - **Explanation**: Finds "1984" despite misspelling, due to fuzzy. Shows score for relevance.

2. Combine with other stages (e.g., sort by score):
   ```javascript
   db.books.aggregate([
     { $search: { index: "default", text: { query: "fiction rebellion", path: ["genre", "description"] } } },
     { $sort: { score: { $meta: "searchScore" } } },
     { $limit: 3 }
   ]).pretty()
   ```

