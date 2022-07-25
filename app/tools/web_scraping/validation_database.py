import requests
import bs4
from validation_lists import letter_map
from time import time
from concurrent.futures import as_completed
from requests_futures import sessions

def scrape_imdb(type, start, stop):

    url = 'https://www.imdb.com/search/title/?title_type=tv_series'
    index = 55
    indicator = '<h3 class="lister-item-header">'

    num = start
    add_on = 10 * ' '
    if type == 'movie':
        indicator = '<span class="lister-item-header">'
        url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie,documentary,short&view=simple&ref_=adv_prv'
        index = 92

    def generate_add_on(num):
        if num == 1:
            return ''
        return '&start=' + str(num)
        
    while add_on != f'&start={stop}':
        
        add_on = generate_add_on(num)
        url = url[:index] + add_on
        

        headers = requests.utils.default_headers()

        headers.update(
            {
                'User-Agent': 'My User Agent 1.0',
            }
        )
        try:
            result = requests.get(url, headers=headers)
        except:
            return

        soup = bs4.BeautifulSoup(result.text, 'lxml')

        terms = str(soup.select('body')[0])
        
        # code
        
        for i in range(len(terms)):
            length = len(indicator)
            if len(terms) - i > length and terms[i:i+length] == indicator:
    
                index = i
                while index < len(terms) and terms[index:index+3] != '</a':
                    index += 1
                name = ''
                index -= 1
                while terms[index] != '>':
                    name += terms[index]
                    index -= 1
                name = name[::-1].replace(u'\xa0', u' ').replace(u'&amp;', u'and').lower()
                name = name.translate(letter_map)
               
                
                
                with open(f'app/tools/web_scraping/{type}.txt', 'a') as f:
                
                    f.write(f'{name}, ')
                    f.close()
        
        
        num += 50
        
def scrape_anime(letters, start=0, stop=950):
    
    for letter in letters:
        num = start
        while num < stop:
            url = f'https://myanimelist.net/anime.php?letter={letter}&show={num}'
            headers = requests.utils.default_headers()

            headers.update(
                {
                    'User-Agent': 'My User Agent 1.0',
                }
            )
            try:
                result = requests.get(url, headers=headers)
            except:
                continue

            soup = bs4.BeautifulSoup(result.text, 'lxml')

            terms = soup.select('strong')

            for term in terms:
                term = str(term)
                
                name = term[8:-9]
                if '(' in name:
                    name = name[:name.index('(') - 1]
                name = name.replace(u'\xa0', u' ').replace(u'&amp;', u'and').lower()
               
                with open(f'app/tools/web_scraping/anime.txt', 'a') as f:
                    try:
                        f.write(f'{name}, ')
                    except:
                        pass
                    f.close()

            
            
            num += 50


movies_db = set(open('app/tools/web_scraping/movie.txt').read().split(', '))


tvshows_db = set(open('app/tools/web_scraping/tvshow.txt').read().split(', '))

anime_db = set(open('app/tools/web_scraping/anime.txt').read().split(', '))




def scrape_english_anime(start, stop):

    urls = [f'https://myanimelist.net/anime/{i}' for i in range(start, stop+1)]
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    with sessions.FuturesSession() as session:
        
        futures = [session.get(url, headers=headers) for url in urls]
        
        for future in as_completed(futures):
            try:

                resp = future.result()
            except:
                
                continue
           
            soup = bs4.BeautifulSoup(resp.text, 'lxml')
            terms = str(soup.select('head')[0])
            
            for i in range(len(terms)):
                
                if terms[i:i+22] == '<meta content="Looking':
                    
                    name = ''
                    index = i
                    
                    while terms[index] != '(':
                        index += 1
                    index += 1
                    
                    while terms[index] != ')':
                        name += terms[index]
                        index += 1
                    if terms[index+3:index+11] == 'Find out':
                  
                        name = name.replace(u'\xa0', u' ').replace(u'&amp;', u'and').replace('&#039;', "'").lower()
                        name = name.translate(letter_map)
                        with open(f'app/tools/web_scraping/anime.txt', 'a') as f:
                            try:
                                f.write(f'{name}, ')
                            except:
                                pass
                            f.close()
                        


                    
                    
                
                    # with open(f'app/tools/web_scraping/anime.txt', 'a') as f:
                    #     try:
                    #         f.write(f'{name}, ')
                    #     except:
                    #         pass
                    #     f.close()S
                  
                    

                    

        
scrape_english_anime(5001, 10000)
# anime_db = set(open('app/tools/web_scraping/anime.txt').read().split(', '))
# for anime in anime_db:
#     if ':' in anime:
#         colon_index = anime.index(':')
#         anime_db.add(anime[:colon_index])
