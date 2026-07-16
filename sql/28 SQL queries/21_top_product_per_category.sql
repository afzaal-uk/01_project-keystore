SELECT product,category, total_units
from(
select
	s_desc AS product,
	prodgrp1 AS category,
	sum(qty) AS total_units,
	ROW_number() OVER (
	PARTITION BY prodgrp1
	ORDER BY sum(qty) DESC
	) AS rank_in_category
FROM SALES_HISTORY 
GROUP BY s_desc, PRODGRP1 
) AS ranked
 WHERE RANK_in_category = 1
 ORDER BY total_units DESC;