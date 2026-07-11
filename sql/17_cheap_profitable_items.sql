SELECT FIRST 10
	s_desc AS product,
	sell,
	sum((sell - cost) * qty) AS total_profit,
	sum(qty) AS units_sold
FROM SALES_HISTORY 
WHERE sell < 2 AND sell > 0
GROUP BY s_desc, sell
ORDER BY total_profit DESC;