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

