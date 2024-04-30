DROP TABLE IF EXISTS films;

-- Create the 'films' table
CREATE TABLE films (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 10)
);

-- Inserting 5 random movies
INSERT INTO films (title, genre, rating) VALUES ('The Grand Odyssey', 'Adventure', 8);
INSERT INTO films (title, genre, rating) VALUES ('Mystery of the Blue Moon', 'Mystery', 7);
INSERT INTO films (title, genre, rating) VALUES ('Gardens of Time', 'Sci-Fi', 9);


