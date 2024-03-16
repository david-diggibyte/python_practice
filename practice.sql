USE employee;
SELECT *
FROM workers;

EXEC sp_rename 'workers', 'worker';  -- table name changed.

CREATE TABLE deparment(
      dept_id INT PRIMARY KEY,
	  dept_name VARCHAR(30));

CREATE TABLE workers(
       id INT ,
	   first_name VARCHAR(30),
	   last_name VARCHAR(30),
	   salary INT,
	   dept_id INT,
	   CONSTRAINT FK_dept FOREIGN KEY (dept_id) REFERENCES deparment(dept_id));

INSERT deparment(dept_id,dept_name)
         VALUES (1,'data engineer'),
		        (2,'HR'),
				(3,'Sales'),
				(4,'digital markating');

SELECT * FROM deparment;

INSERT INTO workers(id,first_name,last_name,salary,dept_id)
            VALUES(1, 'david', 'selvam', 500000, 1),
                  (2, 'dava', 'seelan', 60000, 1),
                  (3, 'Michael', 'john', 55000, 2),
                  (4, 'arokiya', 'mary', 100000, 2),
                  (5, 'david', 'selvam', 10000, 1),
                  (6, 'sathiya', 'selvam', 53000, 3),
                  (7, 'Robert', 'vakkil', 56000, 4),
                  (8, 'david', 'selvam', 54000, 4),
                  (9, 'fathima', 'mary', 57000, 1),
                  (10, 'dava', 'seelan', 59000, 3);

SELECT * FROM workers;

-- order by clause

SELECT *
FROM workers
ORDER BY salary DESC;

SELECT *
FROM workers
ORDER BY first_name ASC;

-- AGGREGATION FUNCTION

SELECT COUNT(*) AS count_id
FROM workers;

SELECT SUM(salary) AS total_salry
FROM workers;

SELECT AVG(salary) AS avg_salary
FROM workers;

SELECT MIN(salary) AS min_salary
FROM workers;

SELECT MAX(salary) AS max_salary
FROM workers;


-- GROUB BY CLAUSE

SELECT first_name
FROM workers
GROUP BY first_name;

SELECT first_name,COUNT(first_name) AS name_count
FROM workers
GROUP BY first_name;

SELECT TOP 10 *
FROM workers;

SELECT salary,count(salary)
FROM workers
GROUP BY salary ;

SELECT first_name,COUNT(first_name) AS count_name
FROM workers
GROUP BY first_name
HAVING COUNT(first_name) > 1;


SELECT first_name,COUNT(first_name) AS count_name
FROM workers
GROUP BY first_name
HAVING COUNT(first_name) > 1
ORDER BY count_name DESC;

USE employee;

SELECT *
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'; -- show all tables in database

SELECT * FROM workers;
SELECT name
FROM sys.tables;   -- show all tables in database

EXEC sp_rename 'deparment','department';  --change the table name

SELECT * FROM department;

INSERT INTO department(dept_id,dept_name)
            VALUES(5,'data analyst'),
			       (6,'advanced analytics'),
				   (7,'power bi devaloper');

SELECT * FROM workers;

INSERT INTO workers(id,first_name,last_name,salary,dept_id)
          VALUES (12,'mariya','nathan',20000,null);



-- joins in SSMS

-- inner join

SELECT *
FROM workers AS w
INNER JOIN department AS d
ON w.dept_id = d.dept_id;

-- left join

SELECT w.*,d.*
FROM workers AS w
LEFT JOIN department AS d
ON w.dept_id = d.dept_id;

-- right join

SELECT w.*,d.*
FROM workers AS W
RIGHT JOIN department AS d
ON w.dept_id = d.dept_id;

-- full join

SELECT w.first_name,w.id,d.dept_id,d.dept_name
FROM workers AS w
FULL JOIN department AS d
ON w.dept_id = d.dept_id;

-- cross join

SELECT *
FROM workers
CROSS JOIN department;



SELECT w.first_name,w.id,d.dept_id,d.dept_name
FROM workers AS w
FULL JOIN department AS d
ON w.dept_id = d.dept_id
WHERE w.id IS NOT NULL;

SELECT TOP 5 w.first_name,w.id,d.dept_id,d.dept_name
FROM workers AS w
FULL JOIN department AS d
ON w.dept_id = d.dept_id
WHERE w.id IS NOT NULL
ORDER BY w.first_name DESC;

-- UNION

SELECT id, first_name
FROM workers
   UNION
SELECT dept_id, dept_name
FROM department;
