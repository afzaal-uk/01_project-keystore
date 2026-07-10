SELECT
	EXTRACT(weekday FROM s_date) AS day_of_week,
	sum(sell * qty) AS total_sales,
	count(*) AS number_of_lines
FROM sales_history
GROUP BY extract(WEEKDAY FROM s_date)
ORDER BY total_sales DESC;