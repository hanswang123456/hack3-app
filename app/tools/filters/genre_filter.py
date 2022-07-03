from get_data import give_movie_data, give_tvshow_data, base_filter

def match_genre(type, genre, results):
    return base_filter(results, type, 'genre', genre)

def match_genre_tvshows(genre, results):
    return match_genre('Series', genre, results)

def match_genre_movies(genre, results):
    return match_genre('Movie', genre, results)





