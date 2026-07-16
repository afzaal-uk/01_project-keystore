select first 10
	S_DESC as product,
	sum((sell - cost) * qty) as total_profit
from sales_history
where prodgrp1 = 'BAKERY'
group by s_desc
order by total_profit desc;