-- schema
CREATE TABLE Employee (
    id INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(25) NOT NULL,
    Salary INT NOT NULL,
    manager_id INT,
    PRIMARY KEY(Id)
);

-- data
INSERT INTO Employee
    (Name, Salary, manager_id)
VALUES
    ('John', 300, 3),
    ('Mike', 200, 3),
    ('Sally', 550, 4),
    ('Jane', 500, 7),
    ('Joe', 600, 7),
    ('Dan', 600, 3),
    ('Phil', 550, NULL)
;

-- Part a.
SELECT 
emp_table.Name
FROM
Employee AS emp_table
INNER JOIN
Employee AS mgr_table 
ON mgr_table.id = emp_table.manager_id
WHERE mgr_table.Salary < emp_table.Salary;

-- Part b.
SELECT 
AVG(Salary)
FROM
Employee
WHERE id NOT IN (SELECT manager_id FROM Employee where manager_id IS NOT NULL);