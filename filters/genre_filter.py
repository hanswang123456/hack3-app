from get_data import give_movie_data, give_tvshow_data

def match_genre(type, genre, results):
    final_results = []
    if type == 'Movie':
        function = give_movie_data
    else:
        function = give_tvshow_data
    for result in results:
        data = function(result)
        cur_genres = data['genres'].split(', ')
        if genre in cur_genres:
            final_results.append(result)
    return final_results

def match_genre_tvshows(genre, results):
    return match_genre('Series', genre, results)

def match_genre_movies(genre, results):
    return match_genre('Movie', genre, results)





