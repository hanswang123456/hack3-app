from get_data import give_movie_data, give_tvshow_data, functions_dict, base_filter

def match_age_group(type : str, age_group : str, results : list):
    return base_filter(results, type, 'age group', age_group)

def match_age_group_tvshows(age_group, results):
    return match_age_group('Series', age_group, results)

def match_age_group_movies(age_group, results):
    return match_age_group('Movie', age_group, results)

