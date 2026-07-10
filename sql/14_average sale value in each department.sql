SELECT 
	prodgrp1 AS category,
	avg(sell * qty) AS avg_sale_value,
	count(*) AS number_of_lines
FROM SALES_HISTORY 
GROUP BY PRODGRP1 
ORDER BY avg_sale_value DESC;