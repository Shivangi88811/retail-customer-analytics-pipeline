# Import pandas for data processing
import pandas as pd

# Import DuckDB database
import duckdb

# Read CSV file
df = pd.read_csv("sample_data.csv")

print("\nOriginal Dataset:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing names
df = df.dropna(subset=["name"])

print("\nCleaned Dataset:")
print(df)

# Connect to DuckDB database
conn = duckdb.connect("customer_data.duckdb")

# Create table and load dataframe
conn.execute("""
CREATE OR REPLACE TABLE customers AS
SELECT * FROM df
""")

# Query database
result = conn.execute("""
SELECT city,
COUNT(*) as total_customers,
AVG(purchase_amount) as avg_purchase
FROM customers
GROUP BY city
""").fetchdf()

print("\nCity Summary:")
print(result)

# Close database connection
conn.close()

print("\nPipeline Completed Successfully")