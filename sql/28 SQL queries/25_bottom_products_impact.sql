SELECT 
	sum(total_revenue) AS bottom_revenue,
	sum(total_profit) AS bottom_profit,
	count(*) AS products_in_bottom
from(
SELECT FIRST 500
	S_desc AS product,
	sum(sell*qty) AS total_revenue,
	sum((sell - cost) * qty) AS total_profit
FROM SALES_HISTORY 
GROUP BY S_DESC 
HAVING sum(qty) > 0
ORDER BY total_revenue ASC 
)
AS bottom_products;
