SELECT sum(product_profit) AS top_10_profit
	FROM (
	SELECT FIRST 10 
s_desc,
sum ((sell - cost) * qty) as product_profit
FROM sales_history
GROUP BY s_desc
ORDER BY product_profit DESC
) AS top_products;

SELECT SUM((SELL - COST) * QTY) AS total_profit
FROM SALES_HISTORY;


--2 diff programmes run both one by one and and then divide the results