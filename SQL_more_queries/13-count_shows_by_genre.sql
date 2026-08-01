-- Counts how many shows are linked to each genre
-- Joins genres to the link table so we can group by genre name
-- Genres with zero shows are excluded automatically since the join finds no rows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
