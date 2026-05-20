SELECT

    c.customer_id,
    c.customer_city,
    c.customer_state,

    COUNT(DISTINCT f.order_id) as total_orders,

    ROUND(
        SUM(f.payment_value), 2
    ) as total_revenue,

    ROUND(
        AVG(f.payment_value), 2
    ) as avg_order_value

FROM {{ ref('fct_orders') }} f

LEFT JOIN {{ ref('dim_customers') }} c
ON f.customer_id = c.customer_id

GROUP BY
    c.customer_id,
    c.customer_city,
    c.customer_state