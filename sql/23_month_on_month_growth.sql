SELECT
    sales_month,
    total_sales,
    previous_month_sales,
    ((total_sales - previous_month_sales) / previous_month_sales) * 100 AS growth_percent
FROM (
    SELECT
        sales_month,
        total_sales,
        LAG(total_sales) OVER (ORDER BY sales_month) AS previous_month_sales
    FROM (
        SELECT
            EXTRACT(MONTH FROM S_DATE) AS sales_month,
            SUM(SELL * QTY) AS total_sales
        FROM SALES_HISTORY
        GROUP BY EXTRACT(MONTH FROM S_DATE)
    ) AS monthly
) AS with_previous
ORDER BY sales_month;