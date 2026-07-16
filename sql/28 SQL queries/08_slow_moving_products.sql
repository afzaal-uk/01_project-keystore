SELECT FIRST 20
	s_desc AS product,
	sum(qty) AS units_sold
FROM SALES_HISTORY 
GROUP BY S_DESC 
HAVING sum(qty) > 0
ORDER BY UNITS_SOLD ASC;