SELECT account_id, COUNT(*) as txn_count
FROM transactions
GROUP BY account_id
HAVING COUNT(*) > 2;

SELECT account_id, SUM(amount) as total_amount
FROM transactions
GROUP BY account_id;

SELECT account_id, SUM(amount) as total_txn_amount
FROM transactions
GROUP BY account_id
HAVING SUM(amount) > 5000;