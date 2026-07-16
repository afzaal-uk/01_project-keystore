SELECT 
	EXTRACT(MONTH FROM s_date) AS sales_month,
	sum(sell * qty) AS total_sales
FROM sales_history
GROUP BY extract(MONTH FROM s_date)
HAVING sum(sell * qty) > (
	SELECT avg(monthly_total)
	FROM (
		SELECT sum(sell * qty) AS monthly_total
		FROM sales_history
		GROUP BY EXTRACT(MONTH FROM s_date)
	) AS monthly_sums
)
ORDER BY total_sales DESC;