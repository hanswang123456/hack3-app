from get_data import give_movie_data, give_tvshow_data

def match_year(type : str, lower_bound : int, upper_bound : int, results : list):
    final_results = []
    if type == 'Movie':
        function = give_movie_data
    else:
        function = give_tvshow_data
    for result in results:
        data = function(result)
        year = int(data['releaseDate'][:4])
        if lower_bound <= year <= upper_bound:
            final_results.append(result)
    return final_results

def match_year_tvshows(lower_bound, upper_bound, results):
    return match_year('Series', lower_bound, upper_bound, results)

def match_year_movies(lower_bound, upper_bound, results):
    return match_year('Movie', lower_bound, upper_bound, results)





