CREATE TABLE transactions (
    id INT,
    account_id INT,
    amount DECIMAL,
    txn_date DATE
);


INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (1, 123, 500, '2003-04-26');

INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (2, 456, 5000, '2013-05-22');

INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (3, 789, 50 ,'2023-07-21');

INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (1, 123, 100, '2003-04-26');

INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (2, 456, 1000, '2013-05-22');

INSERT INTO transactions (id, account_id, amount, txn_date)
VALUES (3, 789, 10, '2003-04-26');

SELECT * FROM accounts
INNER JOIN transactions ON accounts.id = transactions.account_id;