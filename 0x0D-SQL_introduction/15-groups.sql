-- Show the same score in the group
SELECT score, COUNT(score) 'number' FROM second_table GROUP BY score ORDER BY score DESC;
