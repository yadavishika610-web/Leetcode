-- Write your PostgreSQL query statement below
UPDATE Salary
SET sex = CASE
When sex = 'm' then 'f'
when sex = 'f' then 'm'
END;