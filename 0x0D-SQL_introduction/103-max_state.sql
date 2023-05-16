-- display the maximum tempretature of each state
-- orderd by statename


SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
