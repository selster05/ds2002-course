USE sny8gv_db;

-- Inserting data into artists table
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (11, "Black Eyed Peas", "Pop", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (12, "Megan Moroney", "Country", "USA");
INSERT INTO artists (artist_id, artist_name, genre, country) VALUES (13, "Ed Sheeran", "Pop", "UK");

-- Inserting data into albums table
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (111, 11, "The E.N.D.", "2009-06-03");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (112, 12, "Am I Okay?", "2024-07-12");
INSERT INTO albums (album_id, artist_id, album_title, release_date) VALUES (113, 13, "Play", "2025-09-12");
