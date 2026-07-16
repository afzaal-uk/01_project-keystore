select first 15
	s_desc as product,
	sum(qty) as units_sold,
	sum(sell * qty) as total_revenue
from sales_history
where extract (month from s_date) = 12
group by s_desc
order by TOTAL_REVENUE  desc;