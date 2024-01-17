-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
(
  SELECT
    tv_genres.name AS genre,
    COUNT(DISTINCT tv_show_genres.show_id) AS number_of_shows
  FROM
    tv_genres
  LEFT JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY
    genre
  HAVING
    number_of_shows > 0
)
UNION
(
  SELECT
    tv_genres.name AS genre,
    0 AS number_of_shows
  FROM
    tv_genres
  WHERE
    tv_genres.id NOT IN (SELECT DISTINCT genre_id FROM tv_show_genres)
)
ORDER BY
  number_of_shows DESC, genre;
