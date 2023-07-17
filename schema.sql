INSERT INTO users(email, name, admin, password_hash) values ('bruno@bruno.com', 'Bruno', True, '$2b$12$dpR0XWJWtbng0iM0kms57ObGGIyYAH6kQtuE9yXtlgv8tE0owTJgG')
;

SELECT * from users;
SELECT * from expenses;

DROP TABLE expenses
DROP TABLE users CASCADE

SELECT category, sum(amount) as total from expenses where user_id = 2 group by category ORDER BY total DESC;

SELECT payee, date, amount FROM expenses WHERE user_id = 2 AND category = 'Fun';

SELECT category, SUM(amount) as total_amount
FROM expenses
WHERE user_id = 2
  AND category = 'Income'
GROUP BY category;

SELECT 'Expenses' AS category, SUM(amount) AS total_amount
FROM expenses
WHERE user_id = 2
  AND category != 'Income';

  SELECT SUM(amount) AS total
FROM expenses
WHERE user_id = 2
  AND category != 'Income';


