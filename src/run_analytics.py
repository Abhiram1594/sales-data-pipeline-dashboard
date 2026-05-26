from db_connection import get_connection


def run_query(cursor, title, query):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    cursor.execute(query)
    results = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    print(column_names)

    for row in results:
        print(row)


if __name__ == "__main__":
    connection = get_connection()
    cursor = connection.cursor()

    queries = [
        (
            "Total Revenue from Paid Orders",
            """
            SELECT 
                SUM(o.quantity * p.price) AS total_revenue
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            WHERE o.payment_status = 'Paid';
            """
        ),
        (
            "Monthly Revenue Trend",
            """
            SELECT 
                DATE_FORMAT(o.order_date, '%Y-%m') AS month,
                SUM(o.quantity * p.price) AS monthly_revenue
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            WHERE o.payment_status = 'Paid'
            GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
            ORDER BY month;
            """
        ),
        (
            "Top-Selling Products by Quantity",
            """
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
        ),
        (
            "Category-wise Revenue",
            """
            SELECT 
                p.category,
                SUM(o.quantity * p.price) AS category_revenue
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            WHERE o.payment_status = 'Paid'
            GROUP BY p.category
            ORDER BY category_revenue DESC;
            """
        ),
        (
            "Customer Segmentation by Spending",
            """
            SELECT 
                c.customer_id,
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
        ),
        (
            "Fast-Moving Products",
            """
            SELECT 
                p.product_name,
                COUNT(o.order_id) AS number_of_orders,
                SUM(o.quantity) AS total_units_sold
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
            WHERE o.payment_status = 'Paid'
            GROUP BY p.product_name
            ORDER BY number_of_orders DESC, total_units_sold DESC;
            """
        )
    ]

    for title, query in queries:
        run_query(cursor, title, query)

    cursor.close()
    connection.close()