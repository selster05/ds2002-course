-- query.sql takes subset from artists and albums tables and combines data

-- Selecting database
USE sny8gv_db;

-- Combining data from pop artists
SELECT
	artists.artist_name,
	artists.genre,
	albums.album_title,
	albums.release_date
FROM artists
LEFT JOIN albums
	ON artists.artist_id = albums.artist_id
WHERE artists.genre = "Pop";
