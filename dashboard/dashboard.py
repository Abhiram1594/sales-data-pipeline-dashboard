import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sales_analytics"
    )


def fetch_data(query):
    connection = get_connection()
    df = pd.read_sql(query, connection)
    connection.close()
    return df


st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("Sales Data Pipeline & Analytics Dashboard")
st.write("This dashboard shows insights generated from cleaned sales data loaded into MySQL.")

total_revenue_query = """
SELECT 
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid';
"""

monthly_revenue_query = """
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM(o.quantity * p.price) AS monthly_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY month;
"""

top_products_query = """
SELECT 
    p.product_name,
    p.category,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY p.product_name, p.category
ORDER BY total_quantity_sold DESC;
"""

category_revenue_query = """
SELECT 
    p.category,
    SUM(o.quantity * p.price) AS category_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY p.category
ORDER BY category_revenue DESC;
"""

customer_segment_query = """
SELECT 
    c.customer_name,
    c.city,
    SUM(o.quantity * p.price) AS total_spent,
    CASE
        WHEN SUM(o.quantity * p.price) >= 3000 THEN 'High Value'
        WHEN SUM(o.quantity * p.price) >= 1500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY c.customer_id, c.customer_name, c.city
ORDER BY total_spent DESC;
"""

total_revenue_df = fetch_data(total_revenue_query)
monthly_revenue_df = fetch_data(monthly_revenue_query)
top_products_df = fetch_data(top_products_query)
category_revenue_df = fetch_data(category_revenue_query)
customer_segment_df = fetch_data(customer_segment_query)

total_revenue = total_revenue_df["total_revenue"][0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col2.metric("Total Customers", len(customer_segment_df))
col3.metric("Products Sold", int(top_products_df["total_quantity_sold"].sum()))

st.subheader("Monthly Revenue Trend")
st.line_chart(monthly_revenue_df.set_index("month"))

st.subheader("Top-Selling Products")
st.bar_chart(top_products_df.set_index("product_name")["total_quantity_sold"])

st.subheader("Category-wise Revenue")
st.bar_chart(category_revenue_df.set_index("category")["category_revenue"])

st.subheader("Customer Segmentation")
st.dataframe(customer_segment_df)

st.subheader("Raw Analytics Tables")

with st.expander("Monthly Revenue Data"):
    st.dataframe(monthly_revenue_df)

with st.expander("Top Products Data"):
    st.dataframe(top_products_df)

with st.expander("Category Revenue Data"):
    st.dataframe(category_revenue_df)