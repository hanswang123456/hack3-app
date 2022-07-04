from web_scrape import *
from get_urls import *
from time import time

# total = 0
# for i in range(10):
#   start = time()
#   urls = method2('horror movie titles')
#   scrapeUrls(urls)
#   total += (time() - start)
# print(total / 10)

# start = time()
# urls = method2('horror movie titles')
# print(time() - start)
# for url in urls:

#   testing_final(url)
#   print(url)


# print(time() - start)
start = time()
urls = method2('best horror movies with love triangle')
print(urls)
print(base_testing(urls))
print(time() - start)