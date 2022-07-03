from get_data import give_movie_data, give_tvshow_data, base_filter

def match_year(type : str, lower_bound : int, upper_bound : int, results : list):
    return base_filter(results, type, 'year', lower_bound, upper_bound)

def match_year_tvshows(lower_bound, upper_bound, results):
    return match_year('Series', lower_bound, upper_bound, results)

def match_year_movies(lower_bound, upper_bound, results):
    return match_year('Movie', lower_bound, upper_bound, results)





