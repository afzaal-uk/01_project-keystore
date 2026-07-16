SELECT product, category, total_units, rank_in_category
from(
SELECT 
	s_desc AS product,
	prodgrp1 AS category,
	sum(qty) AS total_units,
	rank() OVER (
		PARTITION BY prodgrp1 
		ORDER BY sum(qty) DESC
	) AS rank_in_category
FROM SALES_HISTORY 
GROUP BY s_desc, PRODGRP1 
) AS ranked
WHERE RANK_in_category <= 3
ORDER BY category, rank_in_category;