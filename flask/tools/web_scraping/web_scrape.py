import requests
import bs4
from get_urls import method1

def testing(url):


    names_list = []
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

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


def testing2(url, type='h2'):
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    terms = soup.select(type)

    terms_list = []

    for i in terms:
        cur = str(i)
        for j in range(len(str(i))):
            if cur[j:j+2] == '</':
                index = j - 1
                break

        name = ''
        while cur[index].isalnum() or cur[index] in ['.', "'", ',', '!', '?', ';', ' ', '(', ')', '-']:
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
    null_count = 0
    for i in results:
        if len(i) < 3:
            null_count += 1
    if null_count > 4:
        return False
    return True

def testing_fandom(url):
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    terms = soup.select('h3')

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

def testing_cbr(url):

    names_list = []
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )


    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    terms = soup.select('h2')

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

def testing_imdb(url):
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    terms = soup.select('h3')
  
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

    if 'https://www.fandomspot.' in url:
        res = testing_fandom(url)
        response = check_valid_test(res)
        if response:
            return res

    if 'https://www.imdb' in url:
        res = testing_imdb(url)
        response = check_valid_test(res)
        if response:
            return res

    res = testing(url)

    response = check_valid_test(res)
    if response:
    
        return res
    res = testing2(url)

    response = check_valid_test(res)
    if response:
        
        return res
    res = testing2(url,'h3')

    response = check_valid_test(res)
    if response:
 
        return res

    if 'https://www.cbr.' in url:
        res = testing_cbr(url)
        response = check_valid_test(res)
        if response:
            return res

def scrapeUrls(urls):
  data = set()

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
        data.add(tuple(testing_final(u)))

  return data


