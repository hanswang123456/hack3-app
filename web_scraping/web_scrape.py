from get_urls import method1
import requests
import bs4

def testing():
    
    sample_url = 'https://mangajoys.com/enemies-to-lovers-anime/'
    names_list = []
    result = requests.get(sample_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    terms_list = str(soup.select('body')[0]).split()

    for i in range(len(terms_list)):
        if terms_list[i][-1] == '.':
            if terms_list[i][-2].isnumeric():
                cur_index = i + 1
                anime_name = ''
                while terms_list[cur_index][0] != '<':
                    anime_name += terms_list[cur_index] + ' '
                    cur_index += 1
                new_name = ''
                num_tags = 0
                for j in range(len(anime_name)):
                    if anime_name[j] == '<':
                        num_tags += 1
                    if anime_name[j] == '>':
                        num_tags += 1
                        continue
                    if num_tags % 2 == 0:
                        new_name += anime_name[j]
                    if num_tags == 3:
                        break
                print(new_name)

                names_list.append(anime_name)



    
testing()