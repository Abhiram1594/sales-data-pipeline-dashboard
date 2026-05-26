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
```

## How to Run

### 1. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Clean raw data

```bash
python3 src/data_cleaning.py
```

### 3. Create MySQL database and tables

Open `sql/create_tables.sql` in MySQL Workbench and run the script.

### 4. Load cleaned data into MySQL

```bash
python3 src/load_to_mysql.py
```

### 5. Run analytics queries from Python

```bash
python3 src/run_analytics.py
```

### 6. Start the dashboard

```bash
streamlit run dashboard/dashboard.py
```

## Key Learning Outcomes

This project demonstrates:

- ETL pipeline development
- Data cleaning using Pandas
- MySQL database design
- SQL analytics using joins, grouping, filtering, and aggregation
- Customer segmentation and business insight generation
- Streamlit dashboard creation for data visualization
