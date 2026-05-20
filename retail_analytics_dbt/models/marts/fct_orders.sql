SELECT

    o.order_id,
    o.customer_id,
    o.order_status,
    o.order_purchase_timestamp,

    p.payment_type,
    p.payment_value

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('stg_payments') }} p
ON o.order_id = p.order_id