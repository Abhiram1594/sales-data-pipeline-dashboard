import pandas as pd
import os

RAW_DATA_PATH = "data/raw"
CLEANED_DATA_PATH = "data/cleaned"

os.makedirs(CLEANED_DATA_PATH, exist_ok=True)


def clean_customers():
    customers = pd.read_csv(f"{RAW_DATA_PATH}/customers.csv")

    customers.drop_duplicates(inplace=True)

    customers["customer_name"] = customers["customer_name"].str.strip()
    customers["email"] = customers["email"].str.lower().str.strip()
    customers["city"] = customers["city"].str.strip()
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])

    customers.to_csv(f"{CLEANED_DATA_PATH}/customers_cleaned.csv", index=False)
    print("Customers data cleaned successfully.")


def clean_products():
    products = pd.read_csv(f"{RAW_DATA_PATH}/products.csv")

    products.drop_duplicates(inplace=True)

    products["product_name"] = products["product_name"].str.strip()
    products["category"] = products["category"].str.strip()
    products["price"] = pd.to_numeric(products["price"], errors="coerce")

    products = products.dropna(subset=["price"])
    products = products[products["price"] > 0]

    products.to_csv(f"{CLEANED_DATA_PATH}/products_cleaned.csv", index=False)
    print("Products data cleaned successfully.")


def clean_orders():
    orders = pd.read_csv(f"{RAW_DATA_PATH}/orders.csv")

    orders.drop_duplicates(inplace=True)

    orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce")
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["payment_status"] = orders["payment_status"].str.strip()

    orders = orders.dropna(subset=["quantity"])
    orders = orders[orders["quantity"] > 0]

    orders.to_csv(f"{CLEANED_DATA_PATH}/orders_cleaned.csv", index=False)
    print("Orders data cleaned successfully.")


if __name__ == "__main__":
    clean_customers()
    clean_products()
    clean_orders()
    print("All datasets cleaned and saved in data/cleaned folder.")