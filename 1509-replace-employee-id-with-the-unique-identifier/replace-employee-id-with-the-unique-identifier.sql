# Write your MySQL query statement below
select EU.unique_id, E.name from EmployeeUNI EU right join Employees E
on EU.id = E.id 
