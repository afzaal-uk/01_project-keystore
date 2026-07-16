SELECT 
	prodgrp1 AS category,
	sum((sell - cost) * qty) AS total_profit
FROM SALES_HISTORY 
GROUP BY PRODGRP1 
ORDER BY total_profit DESC;