SELECT FIRST 10
	S_DESC AS product,
	sum((sell - cost) * QTY) AS total_profit,
	sum(sell * qty) AS total_revenue,
	(sum((sell - cost) * qty) / sum(sell * qty)) * 100 AS margin_percent
FROM SALES_HISTORY 
GROUP BY S_DESC
HAVING sum(qty) > 100 AND sum(sell * qty) > 0
ORDER BY margin_percent desc;