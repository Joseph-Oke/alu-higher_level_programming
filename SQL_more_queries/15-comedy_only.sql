-- 15-comedy_only.sql

SELECT tv_shows.title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
  AND tv_genres.id = tv_show_genres.genre_id
  AND tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
