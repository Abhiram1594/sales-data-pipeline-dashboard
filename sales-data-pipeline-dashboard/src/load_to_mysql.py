import pandas as pd
from db_connection import get_connection


def load_customers(cursor):
    customers = pd.read_csv("data/cleaned/customers_cleaned.csv")

    for _, row in customers.iterrows():
        cursor.execute(
            """
            INSERT INTO customers 
            (customer_id, customer_name, email, city, signup_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                int(row["customer_id"]),
                row["customer_name"],
                row["email"],
                row["city"],
                row["signup_date"],
            ),
        )


def load_products(cursor):
    products = pd.read_csv("data/cleaned/products_cleaned.csv")

    for _, row in products.iterrows():
        cursor.execute(
            """
            INSERT INTO products
            (product_id, product_name, category, price)
            VALUES (%s, %s, %s, %s)
            """,
            (
                int(row["product_id"]),
                row["product_name"],
                row["category"],
                float(row["price"]),
            ),
        )


def load_orders(cursor):
    orders = pd.read_csv("data/cleaned/orders_cleaned.csv")

    for _, row in orders.iterrows():
        cursor.execute(
            """
            INSERT INTO orders
            (order_id, customer_id, product_id, quantity, order_date, payment_status)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                int(row["order_id"]),
                int(row["customer_id"]),
                int(row["product_id"]),
                int(row["quantity"]),
                row["order_date"],
                row["payment_status"],
            ),
        )


if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM products")
    cursor.execute("DELETE FROM customers")

    load_customers(cursor)
    load_products(cursor)
    load_orders(cursor)

    connection.commit()

    cursor.close()
    connection.close()

    print("Cleaned data loaded into MySQL successfully.")