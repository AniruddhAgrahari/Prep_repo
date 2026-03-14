SELECT a.owner, COUNT(t.id) as total_txns
FROM accounts a
LEFT JOIN transactions t ON a.id = t.account_id
GROUP BY a.owner;


SELECT a.owner, COUNT(t.id) as total_txns
FROM accounts a
INNER JOIN transactions t ON a.id = t.account_id
GROUP BY a.owner;