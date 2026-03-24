SELECT a.owner, COALESCE(COUNT(t.id), 0) as txn_count 
FROM accounts a 
INNER JOIN transactions t ON a.id = t.account_id 
GROUP BY a.owner;

SELECT a.owner, COALESCE(COUNT(t.id), 0) as txn_count 
FROM accounts a 
LEFT JOIN transactions t ON a.id = t.account_id 
GROUP BY a.owner;

