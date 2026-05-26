USE sales_analytics;

-- 1. Total revenue from paid orders
SELECT 
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid';

-- 2. Monthly revenue trend
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM(o.quantity * p.price) AS monthly_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY month;

-- 3. Top-selling products by quantity
SELECT 
    p.product_name,
    p.category,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY p.product_name, p.category
ORDER BY total_quantity_sold DESC;

-- 4. Category-wise revenue
SELECT 
    p.category,
    SUM(o.quantity * p.price) AS category_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY p.category
ORDER BY category_revenue DESC;

-- 5. Customer segmentation by spending
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

-- 6. Fast-moving products by order frequency
SELECT 
    p.product_name,
    COUNT(o.order_id) AS number_of_orders,
    SUM(o.quantity) AS total_units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.payment_status = 'Paid'
GROUP BY p.product_name
ORDER BY number_of_orders DESC, total_units_sold DESC;