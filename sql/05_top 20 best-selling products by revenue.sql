select 
	first 20
	s_desc AS product,
	sum(sell * qty) AS total_revenue
from sales_history
group by S_DESC 
ORDER BY total_revenue DESC ;
	