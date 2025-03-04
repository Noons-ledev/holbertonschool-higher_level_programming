-- Lists all genres from a database and displays number of shows linked to each of em
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) as show_number
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY show_number DESC;
