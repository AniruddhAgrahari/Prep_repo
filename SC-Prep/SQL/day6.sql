SELECT owner, balance
FROM accounts 
WHERE balance > (SELECT AVG(balance) FROM accounts);

SELECT owner, balance
FROM accounts
WHERE balance > (SELECT AVG(balance) FROM accounts)
ORDER BY balance DESC;