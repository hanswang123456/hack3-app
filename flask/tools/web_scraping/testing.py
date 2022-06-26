from web_scrape import testing_final
from get_urls import method2


def scrapeUrls(urls):
  data = set()

  for u in urls:
    cur_data = testing_final(u)
    if cur_data:
   
        data.add(tuple(cur_data))
    else:
        print(u)

  return data


urls = method2('$anime+like+slime+tensei titles')
res = scrapeUrls(urls)
print(res)
print(len(res))

