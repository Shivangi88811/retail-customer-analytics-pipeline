# Import pandas for data processing
import pandas as pd

# Import DuckDB warehouse
import duckdb

# Create DuckDB connection
conn = duckdb.connect("retail_warehouse.duckdb")

print("\nRetail Data Ingestion Pipeline Started")

# -------------------------------
# Load Customers Dataset
# -------------------------------

customers = pd.read_csv(
    "data/raw/olist_customers_dataset.csv"
)

print("\nCustomers Dataset Loaded")
print(customers.head())

# -------------------------------
# Load Orders Dataset
# -------------------------------

orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

print("\nOrders Dataset Loaded")
print(orders.head())

# -------------------------------
# Load Payments Dataset
# -------------------------------

payments = pd.read_csv(
    "data/raw/olist_order_payments_dataset.csv"
)

print("\nPayments Dataset Loaded")
print(payments.head())

# -------------------------------
# Basic Dataset Profiling
# -------------------------------

print("\nDataset Shapes:")

print(
    f"Customers Rows: {customers.shape[0]}"
)

print(
    f"Orders Rows: {orders.shape[0]}"
)

print(
    f"Payments Rows: {payments.shape[0]}"
)

# -------------------------------
# Check Missing Values
# -------------------------------

print("\nMissing Values Check")

print(
    customers.isnull().sum()
)

print(
    orders.isnull().sum()
)

print(
    payments.isnull().sum()
)

# -------------------------------
# Load Data Into DuckDB
# -------------------------------

conn.execute("""
CREATE OR REPLACE TABLE customers AS
SELECT * FROM customers
""")

conn.execute("""
CREATE OR REPLACE TABLE orders AS
SELECT * FROM orders
""")

conn.execute("""
CREATE OR REPLACE TABLE payments AS
SELECT * FROM payments
""")

print("\nWarehouse Tables Created")

# -------------------------------
# Create Analytics Query
# -------------------------------

query = """

SELECT
    payment_type,
    COUNT(*) as total_transactions,
    ROUND(
        AVG(payment_value), 2
    ) as avg_payment
FROM payments
GROUP BY payment_type
ORDER BY total_transactions DESC

"""

payment_summary = conn.execute(query).fetchdf()

print("\nPayment Analytics Summary")

print(payment_summary)

# -------------------------------

# Customer Order Analytics Table

# -------------------------------

customer_order_query = """

SELECT

    c.customer_id,

    c.customer_city,

    o.order_id,

    o.order_status,

    p.payment_type,

    p.payment_value

FROM customers c

JOIN orders o

ON c.customer_id = o.customer_id

JOIN payments p

ON o.order_id = p.order_id

"""

customer_orders = conn.execute(

    customer_order_query

).fetchdf()

print("\nCustomer Order Analytics Preview")

print(customer_orders.head())

# -------------------------------

# Create Analytics Warehouse Table

# -------------------------------

conn.execute("""

CREATE OR REPLACE TABLE customer_order_summary AS

SELECT * FROM customer_orders

""")

print("\nCustomer Order Summary Table Created")

# Export analytics dataset for Tableau

customer_orders.to_csv(
    "data/processed/customer_order_summary.csv",
    index=False
)

print(
    "\nAnalytics Dataset Exported"
)

# Export dbt mart for Tableau

mart_query = """

SELECT *

FROM customer_revenue_mart

"""

mart_df = conn.execute(

    mart_query

).fetchdf()

mart_df.to_csv(

    "data/processed/customer_revenue_mart.csv",

    index=False

)

print(

    "\nCustomer Revenue Mart Exported"

)

# -------------------------------
# Close Warehouse Connection
# -------------------------------

conn.close()

print("\nRetail Ingestion Pipeline Completed")