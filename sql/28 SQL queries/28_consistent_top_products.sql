SELECT 
	product,
	count(*) AS months_in_top10
from(
SELECT 
	extract(MONTH FROM s_date) AS sales_month,
	s_desc AS product,
	row_number() OVER (
		PARTITION BY EXTRACT(MONTH FROM s_date)
		ORDER BY sum(qty) DESC
	) AS RANK_in_month
	FROM sales_history
	GROUP BY extract(MONTH FROM s_date), s_desc
) AS ranked 
WHERE rank_in_month <= 10
GROUP BY product
ORDER BY months_in_top10 DESC;