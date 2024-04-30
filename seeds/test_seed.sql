-- If table exists then delete it from database
DROP TABLE IF EXISTS test_table;

-- create a test table
CREATE TABLE test_film_table (id SERIAL PRIMARY KEY, name VARCHAR(255));

-- insert record into test table
INSERT INTO test_table (name) VALUES ('first_record');
