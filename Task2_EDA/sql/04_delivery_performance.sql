SELECT ROUND(AVG(FLOOR(julianday(order_delivered_customer_date) - julianday(order_estimated_delivery_date))),2) AS avg_delivery_delay,
ROUND(AVG(CASE WHEN FLOOR(julianday(order_delivered_customer_date) - julianday(order_estimated_delivery_date)) > 0 THEN 1 ELSE 0 END)*100,2) AS late_rate_percent
FROM orders
WHERE order_status = 'delivered';