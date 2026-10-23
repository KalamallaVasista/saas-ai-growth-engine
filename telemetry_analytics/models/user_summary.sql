WITH users AS (
    SELECT * FROM read_csv_auto('../data/raw/users.csv')
),
events AS (
    SELECT * FROM read_csv_auto('../data/raw/event_logs.csv')
),
event_summary AS (
    SELECT 
        user_id,
        COUNT(event_id) AS total_events,
        MIN(event_date) AS first_active_date,
        MAX(event_date) AS last_active_date,
        COUNT(CASE WHEN event_type = 'use_core_feature' THEN 1 END) AS core_feature_clicks,
        COUNT(CASE WHEN event_type = 'upgrade_click' THEN 1 END) AS upgrade_clicks
    FROM events
    GROUP BY user_id
)
SELECT 
    u.user_id,
    u.name,
    u.company,
    u.signup_date,
    COALESCE(e.total_events, 0) AS total_events,
    e.first_active_date,
    e.last_active_date,
    COALESCE(e.core_feature_clicks, 0) AS core_feature_clicks,
    COALESCE(e.upgrade_clicks, 0) AS upgrade_clicks,
    CASE 
        WHEN e.last_active_date < CURRENT_DATE - INTERVAL 14 DAY THEN 'Churn Risk'
        WHEN e.upgrade_clicks > 0 THEN 'High Value'
        ELSE 'Active'
    END AS user_segment
FROM users u
LEFT JOIN event_summary e ON u.user_id = e.user_id
