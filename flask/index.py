from asyncio import constants
from cgi import test
from concurrent.futures import process
from time import process_time
from flask import Flask, render_template, url_for, request
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from googlesearch import search   
import bs4

def siteScraper(keyWord):

    def get_source(url):
        """Return the source code for the provided URL. 
        Args: 
            url (string): URL of the page to scrape.
        Returns:
            response (object): HTTP response object from requests_html. 
        """

        try:
            session = HTMLSession()
            response = session.get(url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def scrape_google(query):

        query = urllib.parse.quote_plus(query)
        response = get_source("https://www.google.co.uk/search?q=" + query)

        links = list(response.html.absolute_links)
        google_domains = ('https://www.google.', 
                        'https://google.', 
                        'https://webcache.googleusercontent.', 
                        'http://webcache.googleusercontent.', 
                        'https://policies.google.',
                        'https://support.google.',
                        'https://maps.google.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        return links

    return scrape_google(keyWord)

#webScraper starts here
sample_url = 'https://www.cbr.com/heartbreaking-anime-happy-endings/'


def testing():


    names_list = []
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(sample_url, headers=headers)
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
                # new_name = ''
                # num_tags = 0
                # for j in range(len(anime_name)):
                #     if anime_name[j] == '<':
                #         num_tags += 1
                #     if anime_name[j] == '>':
                #         num_tags += 1
                #         continue
                #     if num_tags % 2 == 0:
                #         new_name += anime_name[j]
                #     if num_tags == 3:
                #         break
                # # print(new_name)
                # name_v2 = ""
                # for l in new_name:
                #     if l.isalnum() or l in ['.', ',', '!', '?', ';', ' ', '(', ')']:
                #         name_v2 += l
                #     else:
                #         break
                # # print(name_v2)

                # names_list.append(anime_name)
    return names_list


def testing2(type='h2'):


    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    result = requests.get(sample_url, headers=headers)
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

def testing_cbr():

    names_list = []
    headers = requests.utils.default_headers()

    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )


    result = requests.get(sample_url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    terms = soup.select('h2')

    for term in terms:
        term = str(term)
        name = ''
        for i in range(len(term)):
            if term[i:i+7] == '</span>':
                index = i + 8
                break
        while term[index] != '<':

            name += term[index]
            index += 1
        name = name.replace(u'\xa0', u' ')
        name = name.replace(u'&amp;', u'and')
        names_list.append(name)

    return names_list

def webScraper(url):
    sample_url =url
    res = testing()

    response = check_valid_test(res)
    if response:
        print(1)
        return res
    res = testing2()

    response = check_valid_test(res)
    if response:
        print(2)
        return res
    res = testing2('h3')

    response = check_valid_test(res)
    if response:
        print(3)
        return res

    if 'https://www.cbr.' in sample_url:
        res = testing_cbr()
        response = check_valid_test(res)
        if response:
            return res

def give_id(type : str, movie_name : str):
    base_url = f'https://imdb-api.com/en/api/Search{type}/k_2n1kq7r4/'
    movie_response = requests.get(base_url + movie_name)
    
    data = movie_response.json()
    print(data)
    return data['results']

    def match_names(name1, results):
        name1 = ''.join(e for e in name1 if e.isalnum()).lower()
        max_match = [None, 0]
        for result in results:
            name = ''.join(e for e in result['title'] if e.isalnum()).lower()
            if name1 in name:
                match_val = len(name1) / len(name)
                if match_val > max_match[1]:
                    max_match = [result, match_val]
        return max_match[0]




    best_match = match_names(movie_name, data['results'])

    id = best_match['id']
    return id

def give_data(id):
    base_url = 'https://imdb-api.com/en/API/Title/k_2n1kq7r4/'
    link_full = requests.get(base_url + id)

    data = link_full.json()

    return data

def give_tvshow_data(name):
    id = give_id('Series', name)
    print("tv", id)
    return id#give_data(id)

def give_movie_data(name):
    id = give_id('Movie',name)
    print("movie", id)
    return id# give_data(id)


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def my_form_post():
    showNames = []
    showSources = []
    posters = [ 
         "https://m.media-amazon.com/images/M/MV5BZjkxMmMzNzYtODM5ZS00ZGFkLWFlMjItMTA5MTE0ZDZmMzQ5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc2NjA5MTU@._V1_FMjpg_UX1000_.jpg",
          "https://resizing.flixster.com/Z5qVpY6Lw61Vya-StbJXsQx8nMU=/206x305/v2/https://flxt.tmsimg.com/assets/p21666710_b_v13_aa.jpg",
          "https://imdb-api.com/images/original/nopicture.jpg", 
          "https://img1.ak.crunchyroll.com/i/spire4/2ed7860327c766f1cad10c73338a61a91617747114_full.jpg",
           "https://cdn.myanimelist.net/images/anime/6/75642.jpg", 
           "https://upload.wikimedia.org/wikipedia/en/e/e5/Tokyo_Ghoul_volume_1_cover.jpg",
           "https://m.media-amazon.com/images/M/MV5BM2ZkNzgwNzUtMzVkOC00MjUwLWI4YmMtNmViNTcxODZkM2EwXkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_.jpg",
           "https://m.media-amazon.com/images/M/MV5BZmQ5NGFiNWEtMmMyMC00MDdiLTg4YjktOGY5Yzc2MDUxMTE1XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",
           "https://m.media-amazon.com/images/M/MV5BOWExOTEzZWYtYWJhMS00OTM5LWI1M2EtODZiYzE4ZDQ4ZGJkL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
           "https://cdn.anime-planet.com/manga/primary/kiznaiver-1.jpg?t=1625804018",
           "https://cdn.myanimelist.net/images/anime/12/74683.jpg",
           "https://pics.filmaffinity.com/Your_name-406681275-large.jpg",
           





    ]
   
   
    text = request.form['text']
    processed_text = text
    #This would be where we call the siteScraper to find information
    data = siteScraper(processed_text) 
    showNames = []
    showSources = []

    for i in range(len(data)):
        if i>4:
             break
    #     print(data[i]," Scraped Data ",  webScraper(data[i]))
    #     showNames.append(webScraper(data[i]))
        showSources.append(data[i])

    showNames.append(webScraper(sample_url))

    for name in range(len(showNames[0])):
        if name>8:
            break
        currentMovie = showNames[0][name]
        currentMovieSplit = currentMovie.split(" — ", 1)
        currentMovie = currentMovieSplit[0]
        currentMovie.strip()
        #IMDB is currently out of requests...
        #movieData = give_movie_data(currentMovie)
        #seriesData = give_tvshow_data(currentMovie)

        #print(seriesData)
        #print(movieData)
        #if movieData == "[]":
        #    print(seriesData)
        #    posters.append(seriesData)
        #else:
        #    print(movieData)
        #    posters.append(movieData)
        #posters.append(give_movie_data(currentMovie))
    
    print(posters)

    return render_template('listings.html', data = showNames, links = showSources, posters = posters)

if __name__ == "__main__":
    app.run(debug = True)

