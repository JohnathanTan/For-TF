-- Part a.
SELECT 
AVG(Salary)
FROM
Employee
WHERE id NOT IN (SELECT manager_id FROM Employee where manager_id IS NOT NULL);

-- Part b.
SELECT 
emp_table.Name
FROM
Employee AS emp_table
INNER JOIN
Employee AS mgr_table 
ON mgr_table.id = emp_table.manager_id
WHERE mgr_table.Salary < emp_table.Salary;