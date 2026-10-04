SELECT COUNT(DISTINCT orders.order_id) AS total_orders,
ROUND(SUM(price),2) AS total_revenue,
ROUND(SUM(price)/COUNT(DISTINCT orders.order_id),2) AS avg_order_revenue
FROM orders
JOIN order_items ON orders.order_id=order_items.order_id
WHERE order_status = 'delivered';