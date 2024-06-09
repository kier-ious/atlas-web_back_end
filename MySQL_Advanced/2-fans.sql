-- Task2, who's is gonna be??
-- SQL script to rank best bands based on country and fans

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
