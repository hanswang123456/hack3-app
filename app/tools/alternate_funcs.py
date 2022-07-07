def testing_final(url):
    
    soup = base_testing(url)
    terms = ('', '')
    
        
    if 'https://www.fandomspot.' in url or 'https://www.imdb' in url or 'https://www.cbr.' in url:

        if 'https://www.cbr.' in url:
            terms = (soup.select('h2'), 'h2')
            res, response = testing_cbr(terms)
        else:
            terms = (soup.select('h3'), 'h3')
            if 'https://www.fandomspot.' in url:
                res, response = testing_fandom(terms)
            else:
                res, response = testing_imdb(terms)

        if response:
            return res
    def give_final(type):
        final = terms[0]
        if terms[1] != type:
            final = soup.select(type)
        return final

    final = give_final('h2')


    res, response = testing2(final)
    if response:
        return res

    res, response = testing(soup)
    if response:
        return res
    
    final = give_final('h3 ')

    res, response = testing2(final)
    if response:
        return res


def base_filterv2(results, type, func, *args):

    final_results = []
    function = functions_dict[type]
    for result in results:
        data = function(result)
        condition = func(data, *args)
        if condition:
            final_results.append(result)
    return final_results

# sample specific filter funcs
def year_filterv2(data, lower_bound, upper_bound):
    year = int(data['releaseDate'][:4])
    condition = lower_bound <= year <= upper_bound
    return condition

def match_year_tvshows(lower_bound, upper_bound, results):
    return base_filterv2(results, 'Series', year_filterv2, lower_bound, upper_bound)