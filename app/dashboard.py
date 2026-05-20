# Import Streamlit
import streamlit as st

# Import pandas
import pandas as pd

# Import DuckDB
import duckdb

# -------------------------------
# Page Title
# -------------------------------

st.title(
    "Retail Customer Analytics Dashboard"
)

# -------------------------------
# Connect to Warehouse
# -------------------------------

conn = duckdb.connect(
    "retail_warehouse.duckdb"
)

# -------------------------------
# Load Analytics Table
# -------------------------------

query = """

SELECT *
FROM customer_order_summary

"""

df = conn.execute(query).fetchdf()

# -------------------------------
# KPI Metrics
# -------------------------------

total_orders = df["order_id"].nunique()

total_customers = df["customer_id"].nunique()

total_revenue = round(
    df["payment_value"].sum(),
    2
)

avg_order_value = round(
    df["payment_value"].mean(),
    2
)

# -------------------------------
# Display KPIs
# -------------------------------

st.subheader("Business KPIs")

col1, col2 = st.columns(2)

col1.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col2.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col3, col4 = st.columns(2)

col3.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

col4.metric(
    "Average Order Value",
    f"${avg_order_value}"
)

# -------------------------------
# Payment Type Analysis
# -------------------------------

payment_summary = df.groupby(
    "payment_type"
)["payment_value"].sum()

st.subheader(
    "Revenue by Payment Type"
)

st.bar_chart(payment_summary)

# -------------------------------
# Order Status Analysis
# -------------------------------

order_status = df.groupby(
    "order_status"
)["order_id"].count()

st.subheader(
    "Orders by Status"
)

st.bar_chart(order_status)

# -------------------------------
# Dataset Preview
# -------------------------------

st.subheader(
    "Customer Order Summary"
)

st.dataframe(df.head(20))

# -------------------------------
# Close Connection
# -------------------------------

conn.close()