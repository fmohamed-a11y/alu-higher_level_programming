-- Lists only shows that have no genre linked
-- Left join keeps every show, even ones with no match in tv_show_genres
-- Those unmatched shows get genre_id = NULL, which the WHERE clause filters for
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
