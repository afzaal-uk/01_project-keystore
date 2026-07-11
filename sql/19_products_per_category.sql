SELECT
    PRODGRP1 AS category,
    COUNT(DISTINCT S_DESC) AS number_of_products
FROM SALES_HISTORY
GROUP BY PRODGRP1
ORDER BY number_of_products DESC;