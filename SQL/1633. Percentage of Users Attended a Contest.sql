WITH TotalUsers AS (
    SELECT COUNT(*) AS total_users
    FROM Users
),
ContestRegistrations AS (
    SELECT contest_id, COUNT(DISTINCT user_id) AS user_count
    FROM Register
    GROUP BY contest_id
)
SELECT 
    cr.contest_id, 
    ROUND((cr.user_count * 100.0) / tu.total_users, 2) AS percentage
FROM 
    ContestRegistrations cr, 
    TotalUsers tu
ORDER BY 
    percentage DESC, 
    contest_id ASC;
