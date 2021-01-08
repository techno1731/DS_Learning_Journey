-- What years are covered by the dataset?

SELECT DISTINCT year AS 'Years in the study'  
FROM population_years
ORDER BY year DESC;

-- What is the largest population size for Gabon in this dataset?

SELECT *
FROM population_years
WHERE country = 'Gabon'
ORDER BY population DESC
LIMIT 1;

-- What were the 10 lowest population countries in 2005?

SELECT DISTINCT country AS 'Countries with lowest population', year
FROM population_years
WHERE population IS NOT NULL and year = 2005
ORDER BY population ASC 
LIMIT 10;

-- What are all the distinct countries with a population of over 100 million in the year 2010?

SELECT DISTINCT country AS 'Countries with Population over 100 Mill'
FROM population_years
WHERE population IS NOT NULL AND population > 100 AND year = 2010
ORDER BY population DESC;

-- How many countries in this dataset have the word “Islands” in their name?

SELECT COUNT(DISTINCT country) AS 'Number of countries with Islands in their name' 
FROM population_years
WHERE country LIKE '%island%';

-- What is the difference in population between 2000 and 2010 in Indonesia?

SELECT *
FROM population_years
WHERE country = 'Indonesia' AND year = 2000  OR country = 'Indonesia' AND year = 2010;

--What is the difference in population between 2000 and 2010 in Indonesia? - Solution with Joins and Agregation

SELECT (t1.population - t2.population) As 'Pop Diference between 2000 and 2010'
FROM population_years as t1 CROSS JOIN 
     population_years as t2
WHERE t1.country = 'Indonesia' AND t1.year = 2010 AND t2.country = 'Indonesia' and t2.year = 2000;

-- THE END
