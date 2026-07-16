select 
	first 50
	s_desc AS product,
	sum((sell - cost) * qty) AS total_profit
from sales_history
group by S_DESC 
ORDER BY total_profit DESC ;
	