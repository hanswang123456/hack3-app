import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from googlesearch import search   

def method1(query):
    links = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        if 'https://www.youtube.' not in j:
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
                        'https://www.youtube.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        return links

    return scrape_google()

