-- displays the average temperature by city
-- ordered by temperature desc

SELECT cuty, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
