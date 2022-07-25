import requests
import urllib
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from googlesearch import search
import re

to_avoid = (
    'https://www.google.',
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
    'https://www.netflix.',
    'https://www.tiktok.',
    'https://creaturecollege.',
    'https://www.bilibili.',
    'https://www.ranker.',
    'https://play.google.',
    'https://manga.tokyo',
    'https://guessanime.')

def method1(query):
    links = []
  
    for j in search(query, tld="co.in", num=15, stop=15, pause=2):
        if not j.startswith(to_avoid):

            links.add(j)
    return list(links)[:5]

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
        response = get_source("https://www.google.com/search?q=" + query_v2)

        links = list(set(response.html.absolute_links))
      
      
        for url in links[:]:
            if url.startswith(to_avoid):
                links.remove(url)
   
        return links[:5]

    return scrape_google()

def method3(query):
   

    page = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(page.content)
    links = set()

    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        cur = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        try:
            my_link = cur[0]
        except:
            continue
        if not my_link.startswith(to_avoid):
            links.add(my_link)
    return list(links)[:5]
        
