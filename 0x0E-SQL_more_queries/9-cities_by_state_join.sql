-- List all cities contained in the database hbtn_0d_usa
-- Query that lists all cities contained in the database hbtn_0d_usa
SELECT id, name, states.name
FROM cities
INNER JOIN states ON state_id = states.id;
