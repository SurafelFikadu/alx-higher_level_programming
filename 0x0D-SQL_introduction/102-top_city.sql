-- displays the average tempreture of 3 the cities
-- during the month July and August
-- ordered by temperature


SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
