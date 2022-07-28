import requests
import bs4
from concurrent.futures import as_completed
from requests_futures import sessions
from .validation_lists import exceptions
from .validation_database import movies_db, anime_db, tvshows_db

def titleize(name):
    list_name = name.split(' ')
    for i in range(len(list_name)):
        list_name[i] = list_name[i][0].upper() + list_name[i][1:]
    return ' '.join(list_name)

def clean_name(name):
    
    name = name.strip('\'”"“‘’').replace(u'\xa0', u' ').replace(u'&amp;', u'and')
    
    if len(name) > 2 and ((name[0].isdigit() and not name[1].isalpha()) or (name[0] in ['(', '#'] and name[1].isdigit() and not name[2].isalpha())):
        index = 1
        while index < len(name) and not name[index].isalpha():
            index += 1
        name = name[index:]
    if len(name) > 6 and name[-4:].isdigit() and name[-6] == ',':
        name = name[:-6]
        

    for i in range(len(name)):
        if name[i:i+4].lower() == 'from' and name.lower() not in exceptions:
            name = name[i+5:]
            break
        if name[i] == '(':
            new_name = ''
            index = i + 1
            while index < len(name) and name[index] != ')':
                new_name += name[index]
                index += 1
            if new_name[0].isdigit():
               name = name[:i-1]
            else:
                name = new_name
            break
    name = name.strip('\'”"“‘’').replace(u'\xa0', u' ').replace(u'&amp;', u'and')
   
    for i in range(len(name)):

        if name[i] == ':':
          
            if name.lower() not in exceptions:
             
                name = name[:i]
                break
    name = name.lower()

    if name in movies_db or name in anime_db or name in tvshows_db:
        return name
   
    


def check_valid_test(results):
    if len(results) < 5:
    
        return False
    short_count = 0

    for i in results:
        if len(i) < 3:
            short_count += 1
        if len(i) > 100:
            return False

    if short_count > 4:
    
        return False
    return True

def testing(soup):

    
    names_list = []
    
    terms = str(soup.select('body')[0])


    for i in range(len(terms)):

        if terms[i] == '.':

            if terms[i-1].isnumeric() and terms[i+1] == ' ' and (terms[i-2] == '>' or terms[i-3] == '>'):

                cur_index = i + 2
                anime_name = ''
                while terms[cur_index] != '<':
                    anime_name += terms[cur_index]
                    cur_index += 1
                names_list.append(anime_name.strip())
    return names_list, check_valid_test(names_list)


def testing2(terms):


    names_list = []

    for i in terms:
        cur = str(i)
        for j in range(len(str(i))):
            if cur[j:j+3] == '</h':
                index = j - 1
                if cur[j-1] != '>':
                    
                    break
                else:
                    while cur[index] != '<':
                        index -= 1
                    index -= 1

        name = ''
       
        while cur[index].isalnum() or cur[index] in ['—', '.', "'", ',', '!', '?', ';', ' ', '(', ')', '-', '&'] or ord(cur[index]) == 160:

            name += cur[index]
            index -= 1
        name = name[::-1]

        if len(name) > 2:
            if name[2] == '.':
                name = name[4:]

        if len(name) > 1:

            if name[1] == '.':

                name = name[3:]
        names_list.append(name.strip())

    return names_list, check_valid_test(names_list)

def testing2v2(terms):
    names_list = []

    for term in terms:
        term = str(term)
        name = ''

        for i in range(len(term)):
            if term[i] == '>':
                index = i + 1
                while index < len(term) and term[index] != '<':
                    name += term[index]
                    index += 1

        if len(name) > 2:
            if name[2] == '.':
                name = name[4:]

        if len(name) > 1:

            if name[1] == '.':

                name = name[3:]
        names_list.append(name.strip())

    return names_list, check_valid_test(names_list)

def testing_fandom(terms):

    names_list = []

    for i in terms:

        cur = str(i)[::-1]

        name = ''
        for j in range(len(cur)):
            if cur[j] == '<':
                index = j + 1
                break

        while cur[index] != '>':

            name += cur[index]
            index += 1

        names_list.append(name[::-1].strip())

    return names_list, check_valid_test(names_list)

def testing_cbr(terms):

    names_list = []
    for term in terms:
        term = str(term)
        name = ''
        for i in range(len(term)):
            if term[i:i+7] == '</span>':
                index = i + 8
                break
        try:
            index
        except:
            pass
        else:
            while term[index] != '<':

                name += term[index]
                index += 1

        names_list.append(name)

    return names_list, check_valid_test(names_list)

def testing_imdb(terms):

    names_list = []

    for i in terms:

        cur = str(i)[::-1]

        name = ''
        for j in range(len(cur)):
            if cur[j:j+4] == '>a/<':
                index = j + 4
                break

        try:
            cur[index]
        except:
            pass
        else:
            while cur[index] != '>':

                name += cur[index]
                index += 1
                if index >= len(cur):
                    break

        names_list.append(name[::-1].strip())
    
    return names_list[:-3], check_valid_test(names_list[:-3])

def testing_final(soup, url):
    

    if 'https://www.fandomspot.' in url or 'https://www.imdb' in url or 'https://www.cbr.' in url:

        if 'https://www.cbr.' in url:
            terms_h2 = soup.select('h2')
            res, response = testing_cbr(terms_h2)
        else:
            terms_h3 = soup.select('h3')
            if 'https://www.fandomspot.' in url:
                res, response = testing_fandom(terms_h3)
            else:
                res, response = testing_imdb(terms_h3)

        if response:
            return res

    try:
        terms_h2
    except:
        terms_h2 = soup.select('h2')
    
    res, response = testing2v2(terms_h2)
    if response:
        return res

    res, response = testing(soup)
    if response:
        return res
    
    try:
        terms_h3
    except:
        terms_h3 = soup.select('h3')

    res, response = testing2v2(terms_h3)
    if response:
        return res


def scrapeUrls(sites):

    data = set()
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    with sessions.FuturesSession() as session:
        
        futures = [session.get(site, headers=headers) for site in sites]
        
        for future in as_completed(futures):
            try:
                resp = future.result()
            except:
                
                continue
            site = str(resp.url)
            soup = bs4.BeautifulSoup(resp.text, 'lxml')
            
            cur_data = testing_final(soup, site)
            if cur_data:
                
                for j in cur_data:
                    res = clean_name(j)
                    if res:
                        data.add(titleize(res))
            # else:
            #     print(site)
        
        return list(data)

# def scrapeUrls(sites):
#     start = time()
#     total1 = 0
#     total2 = 0
#     data = set()
#     headers = requests.utils.default_headers()

#     headers.update(
#         {
#             'User-Agent': 'My User Agent 1.0',
#         }
#     )

#     session = sessions.FuturesSession()
        
#     futures = [session.get(site, headers=headers) for site in sites]
#     completed = futures
#     print(time() - start)

#     for future in completed:
        
#         cur = time()
#         resp = future.result()
#         site = str(resp.url)
#         soup = bs4.BeautifulSoup(resp.text, 'lxml')
#         end = time()
#         total1 += (end - cur)

#         cur2 = time()
#         cur_data = testing_final(soup, site)
#         if cur_data:
#             data.add(tuple(cur_data))
#         end = time()
#         total2 += (end - cur2)

            
    
#     return total1, total2


