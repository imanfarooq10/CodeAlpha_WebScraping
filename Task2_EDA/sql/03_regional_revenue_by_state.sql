SELECT customers.customer_state AS state,
SUM(order_items.price) AS revenue_by_state
FROM customers
JOIN orders ON orders.customer_id=customers.customer_id
JOIN order_items ON order_items.order_id=orders.order_id
WHERE order_status = 'delivered'
GROUP BY customers.customer_state
ORDER BY revenue_by_state DESC
LIMIT 10;