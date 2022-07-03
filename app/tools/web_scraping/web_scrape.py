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
        name = name.replace(u'\xa0', u' ')
        name = name.replace(u'&amp;', u'and')
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

def testing_final(url):
    
    soup = base_testing(url)

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
    
    res, response = testing2(terms_h2)
    if response:
        return res

    res, response = testing(soup)
    if response:
        return res
    
    try:
        terms_h3
    except:
        terms_h3 = soup.select('h3')

    res, response = testing2(terms_h3)
    if response:
        return res


def scrapeUrls(urls):
  data = set()

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
        data.add(tuple(cur_data))

  return data



