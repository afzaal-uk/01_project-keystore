SELECT 
sales_month,
total_sales,
sum(total_sales) OVER (ORDER BY sales_month) AS running_total
from(
SELECT 
	extract(MONTH FROM s_date) AS sales_month,
	sum(sell * qty) AS total_sales
FROM sales_history
GROUP BY extract(MONTH FROM s_date)
) AS monthly 
ORDER BY sales_month;