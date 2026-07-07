SELECT 
	(SUM((sell - cost) * QTY) / sum(sell * QTY)) * 100 AS profit_margin_percent
FROM SALES_HISTORY ;