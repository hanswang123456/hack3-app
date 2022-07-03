import requests

def give_id(type : str, movie_name : str):
    base_url = f'https://imdb-api.com/en/api/Search{type}/k_2n1kq7r4/'
    movie_response = requests.get(base_url + movie_name)
    data = movie_response.json()
    print(data)
    def match_names(name1, results):
        name1 = ''.join(e for e in name1 if e.isalnum()).lower()
        max_match = [None, 0]
        for result in results:
            name = ''.join(e for e in result['title'] if e.isalnum()).lower()
            if name1 in name or name in name1:
                match_val = len(name1) / len(name)
                if match_val > max_match[1]:
                    max_match = [result, match_val]
        return max_match[0]




    best_match = match_names(movie_name, data['results'])
    if best_match == None:
        return False
    id = best_match['id']
    return id

def give_data(id):
    base_url = 'https://imdb-api.com/en/API/Title/k_2n1kq7r4/'
    link_full = requests.get(base_url + id)
    data = link_full.json()
    return data

def give_tvshow_data(name):
    id = give_id('Series', name)
    if id:
        return give_data(id)

def give_movie_data(name):
    id = give_id('Movie', name)
    if id:
        return give_data(id)

functions_dict = {
    'Movie' : give_movie_data,
    'Series' : give_tvshow_data
}

def base_filter(results, type, *filter_type):

    final_results = []
    function = functions_dict[type]
    for result in results:
        data = function(result)
        if filter_type[0] == 'year':
            year = int(data['releaseDate'][:4])
            condition = filter_type[1] <= year <= filter_type[2]
        elif filter_type[0] == 'genre':
            cur_genres = data['genres'].split(', ')
            condition = filter_type[1] in cur_genres
        else:
            cur_age_group = data['contentRating']
            condition = cur_age_group == filter_type[1]
        if condition:
            final_results.append(result)
    return final_results

# def base_filterv2(results, type, func, *args):

#     final_results = []
#     function = functions_dict[type]
#     for result in results:
#         data = function(result)
#         condition = func(data, *args)
#         if condition:
#             final_results.append(result)
#     return final_results

# # sample specific filter funcs
# def year_filterv2(data, lower_bound, upper_bound):
#     year = int(data['releaseDate'][:4])
#     condition = lower_bound <= year <= upper_bound
#     return condition

# def match_year_tvshows(lower_bound, upper_bound, results):
#     return base_filterv2(results, 'Series', year_filterv2, lower_bound, upper_bound)

