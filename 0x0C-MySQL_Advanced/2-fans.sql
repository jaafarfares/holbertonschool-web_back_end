-- script that ranks county's origins of bands
SELECT origin, SUM(num_members) AS nb_fans
FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;
