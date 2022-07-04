import requests
import urllib

from requests_html import HTMLSession
from googlesearch import search

URL_LIMIT = 5

def method1(query):
    links = []
    avoid_list = ['https://en.wikipedia.',
    'https://www.youtube.', 
    'https://myanimelist.', 
    'https://www.reddit.', 
    'https://www.quora.', 
    'https://translate.google.', 
    'https://editorial.rottentomatoes.', 
    'https://www.coolmoviez.',
    'https://www.netflix.']
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        for i in avoid_list:
            if i in j:
                break
        else:
            links.append(j)
    return links

def method2(query):

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

    def scrape_google():

        query_v2 = urllib.parse.quote_plus(query)
        response = get_source("https://www.google.co.uk/search?q=" + query_v2)

        links = list(response.html.absolute_links)
        google_domains = ('https://www.google.',
                        'https://google.',
                        'https://webcache.googleusercontent.',
                        'http://webcache.googleusercontent.',
                        'https://policies.google.',
                        'https://support.google.',
                        'https://maps.google.',
                        'https://www.youtube.',
                        'https://en.wikipedia.',
                        'https://myanimelist.',
                        'https://www.reddit.',
                        'https://www.quora.',
                        'https://translate.google.',
                        'https://editorial.rottentomatoes.',
                        'https://www.coolmoviez.',
                        'https://www.netflix.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        return links[:URL_LIMIT]

    return scrape_google()
