-- Show all list with the name California.
SELECT id, name FROM cities
WHERE state_id = (
SELECT id FROM states WHERE name = 'California');
