-- List all records without MULL values
SELECT `score`, `name` FROM second_table WHERE `name` != NULL ORDER BY score DESC;
