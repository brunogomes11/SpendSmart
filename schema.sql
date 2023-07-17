INSERT INTO users(email, name, admin, password_hash) values ('bruno@bruno.com', 'Bruno', True, '$2b$12$dpR0XWJWtbng0iM0kms57ObGGIyYAH6kQtuE9yXtlgv8tE0owTJgG')
;

SELECT * from users;
SELECT * from expenses;

DROP TABLE expenses
DROP TABLE users CASCADE