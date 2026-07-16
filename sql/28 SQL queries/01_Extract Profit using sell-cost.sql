SELECT 
	extract(YEAR FROM S_DATE) AS sales_year,
	sum((SELL - cost)* qty) AS total_profit
FROM SALES_HISTORY
GROUP BY EXTRACT (year FROM S_DATE)
ORDER BY sales_year;