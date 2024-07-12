-- SCript that ranks origins of bands
-- ordered by the number of (non - UNIQUE) fans
SELECT DISTINCT origin, SUM(fans) AS nb_fans FROM  metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
