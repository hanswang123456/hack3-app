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


# urls = method2(input())
res = scrapeUrls(['https://www.reddit.com/r/anime/comments/uw995l/animes_with_likeable_and_caring_male_mcs/', 'https://www.ranker.com/list/most-beloved-anime-characters/anna-lindwasser', 'https://bakabuzz.com/the-10-best-anime-where-the-mc-is-loved-and-respected-by-everyone/', 'https://www.lifewire.com/best-anime-4156813', 'https://www.reddit.com/r/anime/comments/8if533/anime_with_likable_mc/'])
print(res)
print(len(res))

