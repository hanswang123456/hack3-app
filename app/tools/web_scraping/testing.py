import web_scrape_old
import web_scrape
from get_urls import *
from time import time

movie_queries = [['horror', 'action', 'romance', 'alien', 'fantasy'] * 5, 'movies']
anime_queries = [['badass mc', 'cool mc', 'bitersweet ending', 'early romance'] * 5, 'anime']
tvshow_queries = [['bitersweet ending', 'happy ending', 'love triangle', 'high school'] * 5, 'tv shows']
big = [movie_queries, anime_queries, tvshow_queries]

total1 = 0
total2 = 0
total_url = 0
max1 = 0
max2 = 0
count1 = 0
count2 = 0
initial = time()
for i in big:
    key_word = i[1]
    for query in i[0]:
        cur = time()
        urls = method2(f'{query} {key_word}')
        diff_url = time() - cur
        total_url += diff_url
        cur = time()
        count1 += web_scrape.scrapeUrls(urls)
        dif1 = time() - cur
     
        if dif1 > max1:
            max1 = dif1
        total1 += dif1
        cur = time() 
        count2 += web_scrape_old.scrapeUrls(urls)
        dif2 = time() - cur
       
        if dif2 > max2:
            max2 = dif2
        total2 += dif2
print(time() - initial)
print(total_url / 65)
print(max1)
print(max2)
print(count1, count2)
print(total1 / (65 - count1))
print(total2 / (65 - count2))