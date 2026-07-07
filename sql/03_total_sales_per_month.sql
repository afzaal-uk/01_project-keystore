SELECT 
	EXTRACT(MONTH FROM S_DATE) AS sales_month,	
	sum(sell * qty) AS total_sales
FROM Sales_history
GROUP BY EXTRACT (MONTH FROM s_date)
ORDER BY total_sales DESC;
	