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


USE employee;
CREATE TABLE student(
     id INT,
	 name VARCHAR(30),
	 department VARCHAR(30),
	 marks INT,
	 HOD VARCHAR(30),
	 collage VARCHAR(30));

EXEC sp_help 'student';

SELECT name
FROM sys.tables;

SELECT *
FROM INFORMATION_SCHEMA.TABLES;

-- add one column

ALTER TABLE student
ADD semaster VARCHAR(30);

-- change column name

EXEC sp_rename 'student.semaster','finalsemaster','COLUMN';

-- drop the column name

ALTER TABLE student
DROP COLUMN finalsemaster;

-- add the consraints

-- adding the peimary key

SELECT * FROM student;
INSERT INTO student(id,name,department,marks,HOD,collage)
       VALUES(1,'david','cse',80,'rober selvam','govt clg');

-- adding not null constraint

ALTER TABLE student
ALTER COLUMN id INT NOT NULL;

ALTER TABLE student
ALTER COLUMN id INT NULL;

-- adding primary key

ALTER TABLE student
ADD CONSTRAINT PK_stud
PRIMARY KEY(id);

ALTER TABLE student
DROP CONSTRAINT PK_stud;

-- WINDOW FUNCTION AND SUBQUERY

USE ecommerce;

CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    manager_id INT
);

INSERT INTO employees (employee_id, first_name, last_name, department, salary, manager_id)
VALUES
    (1, 'John', 'Doe', 'Finance', 60000.00, NULL),
    (2, 'Jane', 'Smith', 'Finance', 55000.00, 1),
    (3, 'Alice', 'Johnson', 'HR', 50000.00, NULL),
    (4, 'Bob', 'Williams', 'HR', 48000.00, 3),
    (5, 'Charlie', 'Brown', 'IT', 70000.00, NULL),
    (6, 'David', 'Lee', 'IT', 65000.00, 5),
    (7, 'Emma', 'Garcia', 'IT', 60000.00, 5),
    (8, 'Michael', 'Miller', 'Sales', 55000.00, NULL),
    (9, 'Sophia', 'Wilson', 'Sales', 52000.00, 8),
    (10, 'Olivia', 'Martinez', 'Sales', 48000.00, 8),
    (11, 'James', 'Taylor', 'Marketing', 60000.00, NULL),
    (12, 'Daniel', 'Anderson', 'Marketing', 58000.00, 11),
    (13, 'Ella', 'Thomas', 'Marketing', 55000.00, 11),
    (14, 'William', 'Harris', 'Engineering', 72000.00, NULL),
    (15, 'Victoria', 'White', 'Engineering', 68000.00, 14),
    (16, 'Liam', 'Clark', 'Engineering', 65000.00, 14);

	SELECT * FROM employees;

INSERT INTO employees(employee_id, first_name, last_name, department, salary, manager_id)
             VALUES(6, 'David', 'Lee', 'IT', 65000.00, 5),
			       (7, 'Emma', 'Garcia', 'IT', 60000.00, 5),
				   (10, 'Olivia', 'Martinez', 'Sales', 48000.00, 8),
				   (4, 'Bob', 'Williams', 'HR', 48000.00, 3),
				   (9, 'Sophia', 'Wilson', 'Sales', 52000.00, 8),
				   (3, 'Alice', 'Johnson', 'HR', 50000.00, NULL),
				   (15, 'Victoria', 'White', 'Engineering', 68000.00, 14),
                   (16, 'Liam', 'Clark', 'Engineering', 65000.00, 14);

SELECT *
FROM ( SELECT first_name,salary,
              ROW_NUMBER() OVER(PARTITION BY first_name ORDER BY salary) AS latest_salary
	 FROM employees) AS sub
WHERE latest_salary = 1
ORDER BY first_name ASC;

SELECT first_name,salary FROM employees ORDER BY first_name;



SELECT department,CONCAT(first_name,' ',last_name) AS full_name,salary,
       row_number() over( partition by department order by employee_id desc) AS row_number
FROM employees;

WITH cte1 AS (
SELECT first_name ,department,
       RANK() OVER(PARTITION BY department ORDER BY first_name) AS rankk
FROM employees)
SELECT * FROM cte1 WHERE rankk = 1;

WITH cte AS  (
SELECT first_name,department,
       ROW_NUMBER() OVER(PARTITION BY department ORDER BY first_name) AS rno
FROM employees )
SELECT * FROM cte WHERE rno = 1;

SELECT *
FROM (
    SELECT
        first_name,
        department,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY first_name) AS rno
    FROM employees
) AS subquery
WHERE rno = 1;

SELECT * FROM employees;
SELECT department,count(department),sum(salary)
FROM employees
GROUP BY department;


SELECT *
FROM ( SELECT first_name,department,salary,
      NTILE(5) OVER(ORDER BY employee_id) AS ntilee
	  FROM employees) AS ntileee;