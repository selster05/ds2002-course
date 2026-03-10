-- initialize.sql creates two tables - an artists table and an albums table

-- Drop tables
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

-- Create artists table
CREATE TABLE artists (
	artist_id INT PRIMARY KEY,
	artist_name VARCHAR(100) NOT NULL,
	genre VARCHAR(100) NOT NULL,
	country VARCHAR(100) NOT NULL
);

-- Create albums table
CREATE TABLE albums (
	album_id INT PRIMARY KEY,
	artist_id INT NOT NULL,
	album_title VARCHAR(100) NOT NULL,
	release_date DATE NOT NULL,
	FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Inserting data into artists table
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (1, "Taylor Swift", "Pop", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (2, "Sabrina Carpenter", "Pop", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (3, "Depeche Mode", "Rock", "UK");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (4, "Harry Styles", "Pop", "UK");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (5, "Kacey Musgraves", "Country", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (6, "Bad Bunny", "Rap", "Puerto Rico");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (7, "The Beatles", "Rock", "UK");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (8, "Queen", "Rock", "UK");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (9, "Noah Kahan", "Folk", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (10, "Zach Bryan", "Country", "USA");

-- Inserting data into albums table
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (101, 1, "Folklore", "2020-07-24");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (102, 1, "Lover", "2019-08-23");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (103, 2, "Man's Best Friend", "2025-08-29");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (104, 4, "Harry's House", "2022-05-20");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (105, 8, "A Night at the Opera", "1975-11-21");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (106, 9, "Busyhead", "2019-06-14");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (107, 6, "Un Verano Sin Ti", "2022-05-06");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (108, 10, "Elisabeth", "2020-05-08");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (109, 4, "Fine Line", "2019-12-13");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (110, 5, "Golden Hour", "2018-03-30");
