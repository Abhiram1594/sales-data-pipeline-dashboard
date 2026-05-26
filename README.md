# Sales Data Pipeline & Analytics Dashboard

This project is a Python, SQL, MySQL, and Pandas based data pipeline that cleans raw sales data, loads it into a MySQL database, runs analytics queries, and displays business insights using a Streamlit dashboard.

## Tech Stack

- Python
- Pandas
- MySQL
- SQL
- Streamlit
- Matplotlib

## Project Features

- Cleaned raw customer, product, and order CSV files using Pandas
- Loaded cleaned data into MySQL tables
- Created relational schema using primary and foreign keys
- Wrote SQL analytics queries using joins, grouping, filtering, aggregation, and CASE statements
- Generated insights such as:
  - Total revenue
  - Monthly revenue trend
  - Top-selling products
  - Category-wise revenue
  - Customer segmentation
  - Fast-moving products
- Built an interactive Streamlit dashboard for visualization

## Project Structure

```txt
sales-data-pipeline-dashboard/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── sql/
│   ├── create_tables.sql
│   ├── analytics_queries.sql
│   └── indexes.sql
│
├── src/
│   ├── data_cleaning.py
│   ├── db_connection.py
│   ├── load_to_mysql.py
│   └── run_analytics.py
│
├── dashboard/
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
