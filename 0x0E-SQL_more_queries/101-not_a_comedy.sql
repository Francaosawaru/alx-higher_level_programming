-- lists shows that don't belong to Comedy genre
SELECT tv_shows.title
[2;2R[>77;30604;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title
	FROM tv_shows
     	JOIN tv_show_genres
     	     ON tv_show_genres.show_id = tv_shows.id
     	JOIN tv_genres
     	     ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.id
) comedy_shows ON comedy_shows.title = tv_shows.title
WHERE comedy_shows.title is NULL
ORDER BY tv_shows.title;
