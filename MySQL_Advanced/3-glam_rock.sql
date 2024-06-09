-- Task3, Glam rock
/* Write a SQL script that lists all bands with Glam
rock as their main style, ranked by their longevity */
SELECT
    band_name,
    IFNULL(YEAR(split) - YEAR(formed), 0) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
