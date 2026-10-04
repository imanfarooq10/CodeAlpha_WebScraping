SELECT product_category.product_category_name_english,
SUM (order_items.price) AS total_revenue
FROM orders
JOIN order_items ON orders.order_id=order_items.order_id
JOIN products ON products.product_id=order_items.product_id
JOIN product_category ON products.product_category_name=product_category.product_category_name
WHERE order_status = 'delivered'
GROUP BY product_category.product_category_name
ORDER BY total_revenue DESC
LIMIT 10;