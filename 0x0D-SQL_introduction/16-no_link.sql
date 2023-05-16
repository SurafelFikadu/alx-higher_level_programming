-- lista all records that is in a table except those who do not have name value

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
