from web_scrape import testing_final
from get_urls import method1

def scrapeUrls(urls):
  data = []

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
        data.append(testing_final(u))
    else:
        print(u)
  return data
urls = method1(input())
print(scrapeUrls(urls))
