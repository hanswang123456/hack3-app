import requests
import bs4
from time import time

def base_testing(url):
    start = time()
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(url, headers=headers)
    print(time() - start)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    return soup

def testing(soup):

    
    names_list = []
    terms_list = str(soup.select('body')[0])

    for i in range(len(terms_list)):

        if terms_list[i] == '.':

            if terms_list[i-1].isnumeric() and terms_list[i+1] == ' ' and (terms_list[i-2] == '>' or terms_list[i-3] == '>'):

                cur_index = i + 2
                anime_name = ''
                while terms_list[cur_index] != '<':
                    anime_name += terms_list[cur_index]
                    cur_index += 1
                names_list.append(anime_name.strip())
    return names_list


def testing2(terms):


    terms_list = []

    for i in terms:
        cur = str(i)
        for j in range(len(str(i))):
            if cur[j:j+3] == '</h':
                index = j - 1
                break

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
        terms_list.append(name.strip())

    return terms_list

def check_valid_test(results):
    if len(results) < 5:
        return False
    short_count = 0

    for i in results:
        if len(i) < 3:
            short_count += 1
        # if len(i) > 100:
        #     return False

    if short_count > 4:
        return False
    return True

def testing_fandom(terms):

    terms_list = []

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

        terms_list.append(name[::-1].strip())

    return terms_list

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
        name = name.replace(u'\xa0', u' ')
        name = name.replace(u'&amp;', u'and')
        names_list.append(name)

    return names_list

def testing_imdb(terms):
    print(terms)
    terms_list = []

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

        terms_list.append(name[::-1].strip())

    return terms_list[:-3]

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
    # alternatively try except can be used to check existence of h2 and h3 terms
    final = terms[0]
    if terms[1] != 'h2':
        final = soup.select('h2')


    res, response = testing2(final)
    if response:
        return res

    res, response = testing(soup)
    if response:
        return res
    
    final = terms[0]
    if terms[1] != 'h3':
        final = soup.select('h3')

    res, response = testing2(final)
    
    if response:
        return res


def scrapeUrls(urls):
  data = set()

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
        data.add(tuple(cur_data))

  return data



url = 'https://www.imdb.com/search/title/?genres=action&explore=title_type,genres&sort=alpha,asc'
soup = base_testing(url)


terms_h3 = soup.select('h3')
print(testing_imdb(terms_h3))