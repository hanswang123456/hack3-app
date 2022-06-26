from get_data import give_movie_data, give_tvshow_data

def match_age_group(type : str, age_group : str, results : list):
    final_results = []
    if type == 'Movie':
        function = give_movie_data
    else:
        function = give_tvshow_data
    for result in results:
        data = function(result)
        cur_age_group = data['contentRating']
        if cur_age_group == age_group:
            final_results.append(result)
    return final_results

def match_age_group_tvshows(age_group, results):
    return match_age_group('Series', age_group, results)

def match_age_group_movies(age_group, results):
    return match_age_group('Movie', age_group, results)

