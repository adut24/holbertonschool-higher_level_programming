-- List all the cities of California that can be found in the database hbtn_0d_usa
-- Query that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE states.name = "California")
ORDER BY cities.id ASC;
