SELECT
    PRODGRP1 AS category,
    SUM(SELL * QTY) AS total_revenue,
    SUM((SELL - COST) * QTY) AS total_profit
FROM SALES_HISTORY
GROUP BY PRODGRP1
ORDER BY total_revenue DESC;