
DROP TABLE transactions;

CREATE TABLE transactions (
    txn_id INT, 
    account_id VARCHAR(10),
    amount DECIMAL(10, 2),
    txn_date DATE
);

INSERT INTO transactions VALUES
(1, 'ACC001', 500, '2024-01-01'),
(2, 'ACC001', 300, '2024-01-05'),
(3, 'ACC001', 500, '2024-01-03'),
(4, 'ACC002', 1000, '2024-01-02'),
(5, 'ACC002', 750.00, '2024-01-04'),
(6, 'ACC002', 750.00, '2024-01-06');



SELECT * FROM (
SELECT 
account_id,
txn_date,
ROW_NUMBER() OVER (PARTITION BY account_id ORDER BY txn_date DESC) as rn
FROM transactions
) AS ranked
WHERE rn = 1;

SELECT 
txn_id,
account_id,
amount,
RANK() OVER (ORDER BY amount DESC) as rnk
FROM transactions;

SELECT
txn_id,
account_id,
amount,
DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rnk 
FROM transactions;

