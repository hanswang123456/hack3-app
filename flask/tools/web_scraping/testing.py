from web_scrape import testing_final
from get_urls import method1


def scrapeUrls(urls):
  data = set()

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
        data.add(tuple(testing_final(u)))
    else:
        print*u

  return data


urls = method1(input())
print(scrapeUrls(urls))
