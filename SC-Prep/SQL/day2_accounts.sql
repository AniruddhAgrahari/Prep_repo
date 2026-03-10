CREATE TABLE accounts
(id INT PRIMARY KEY, 
typer VARCHAR(20),
balance DECIMAL(10, 2),
owner VARCHAR(50));

INSERT INTO accounts (id, typer, balance, owner) 
VALUES (1, 'Savings', 5000.00, 'Aniruddh');

INSERT INTO accounts (id, typer, balance, owner)
VALUES (2, 'Current', 10000.0, 'Ani');

INSERT INTO accounts (id, typer, balance, owner)
VALUES (3, 'Savings', 50.0, 'Rajiv');

INSERT INTO accounts (id, typer, balance, owner)
VALUES (4, 'Current', 100.0, 'Harshal');

INSERT INTO accounts (id, typer, balance, owner)
VALUES(5, 'Savings', 200.0, 'Vaibhav');

SELECT * FROM ACCOUNTS WHERE BALANCE >= 10000;

