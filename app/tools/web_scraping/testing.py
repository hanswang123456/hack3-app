import web_scrapev2
import web_scrape
from get_urls import *
from time import time

def scrapeUrls(urls, function):
  
  data = set()
  for u in urls:
    cur_data = function(u)
    if cur_data:
   
        data.add(tuple(cur_data))


  return data
total = 0
for i in range(10):
  start = time()
  urls = method2('anime bitersweet titles')
  scrapeUrls(urls, web_scrapev2.testing_final)
  total += (time() - start)
print(total / 10)

total = 0
for i in range(10):
  start = time()
  urls = method2('anime bitersweet titles')
  scrapeUrls(urls, web_scrape.testing_final)
  total += (time() - start)
print(total / 10)

