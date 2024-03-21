from pymongo import MongoClient
import pandas as pd
import random

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Create a new database
db = client['sales_database']

# Access the collection
sales_collection = db['sales']

# Define a function to generate random sales data and add it to the collection
def generate_sales_data(num_transactions):
    sales_data = []
    products = ['Product A', 'Product B', 'Product C']
    for _ in range(num_transactions):
        transaction = {
            'date': '2024-03-21',  # Assuming all transactions happen on the same date for simplicity
            'product': random.choice(products),
            'quantity': random.randint(1, 10),
            'total_amount': round(random.uniform(10.0, 100.0), 2)
        }
        sales_data.append(transaction)
    # Insert sales data into the collection
    sales_collection.insert_many(sales_data)
    print("Sales data added successfully.")

# Define a function to analyze sales data
def analyze_sales():
    # Retrieve sales data from the collection
    sales_data = list(sales_collection.find())
    
    # Convert sales data to a DataFrame for analysis
    df = pd.DataFrame(sales_data)
    
    # Perform data analysis
    total_sales = df['total_amount'].sum()
    average_quantity = df['quantity'].mean()
    most_sold_product = df['product'].value_counts().idxmax()
    
    # Print analysis results
    print("Total sales amount:", total_sales)
    print("Average quantity sold per transaction:", average_quantity)
    print("Most sold product:", most_sold_product)

# Generate and add sales data to the collection
generate_sales_data(100)

# Analyze the sales data
analyze_sales()

# Close the connection to the MongoDB server
client.close()