import requests

def give_id(type : str, movie_name : str):
    base_url = f'https://imdb-api.com/en/api/Search{type}/k_2n1kq7r4/'
    movie_response = requests.get(base_url + movie_name)
    data = movie_response.json()
    print(data)

    def match_names(name1, results):
        if results == None:
            return
        if len(results) == 1:
            return results[0]
        name1 = ''.join(e for e in name1 if e.isalnum()).lower()
        max_match = [None, 0]
        for result in results:
            name = ''.join(e for e in result['title'] if e.isalnum()).lower()
            if name1 in name or name in name1:
                match_val = len(name1) / len(name)
                if match_val > max_match[1]:
                    max_match = [result, match_val]
        return max_match[0]




    best_match = match_names(movie_name, data['results'])
    if best_match == None:
        return False
    id = best_match['id']
    return id

def give_data(id):
    base_url = 'https://imdb-api.com/en/API/Title/k_2n1kq7r4/'
    link_full = requests.get(base_url + id)
    data = link_full.json()
    return data

def give_tvshow_data(name):
    id = give_id('Series', name)
    if id:
        return give_data(id)

def give_movie_data(name):
    id = give_id('Movie', name)
    if id:
        return give_data(id)

functions_dict = {
    'Movie' : give_movie_data,
    'Series' : give_tvshow_data
}

def base_filter(results, type, *filter_type):

    final_results = []
    function = functions_dict[type]
    for result in results:
        data = function(result)
        if filter_type[0] == 'year':
            year = int(data['releaseDate'][:4])
            condition = filter_type[1] <= year <= filter_type[2]
        elif filter_type[0] == 'genre':
            cur_genres = data['genres'].split(', ')
            condition = filter_type[1] in cur_genres
        else:
            cur_age_group = data['contentRating']
            condition = cur_age_group == filter_type[1]
        if condition:
            final_results.append(result)
    return final_results

data = [['Social', 'Main navigation', 'Related Stories', 'The best streaming services in 2021', 'The Best Christmas Movies of All Time', 'Movie Santas Ranked Least to Most Jolly', 'Most widely watched but universally hated movies of all time', 'Worst to First', 'best religious movies, according to critics', 'The Tree of Life', 'Black Narcissus', 'The Wild Pear Tree', 'The Master', 'Divine Love', 'The Wicker Man', 'Maria Full of Grace', 'The Seventh Seal', 'Wild Strawberries', 'Minari', 'Hard to Be a God', 'Ida', 'Son of Saul', 'Atanarjuat', 'Moolaadé', 'The Rider', 'Timbuktu', 'Spotlight', 'Sita Sings the Blues', 'There Will Be Blood', 'Lady Bird', 'Apocalypse Now', 'Schindler’s List', 'The Grapes of Wrath', 'Years a Slave', 'Trending Now', 'Experts rank the best U.S. presidents of all time', "best 'SNL' episodes", 'best space movies of all time', 'Top 100 country songs of all time', 'Footer', 'Social', 'best religious movies, according to critics'], ['A Promise', 'Barabbas', 'The Bible', 'Bilal', 'Bruce Almighty', 'Bu Ken Qu Guan Yin aka Avalokiteshvara', 'China Cry', 'Conspiracy of Silence', 'Courageous', 'Evil', 'Elmer Gantry', 'Hell', 'Evan Almighty', 'Facing the Giants', 'Fireproof', 'Gabriel', "God's Not Dead", 'Heaven Is for Real', 'Home Run', 'Islam', 'Jacob', "Giacobbe, l'uomo che lottò con Dio", 'Jonah', 'Joan of Arc', 'Joan of Arc', "La passion de Jeanne d'Arc", 'Joan of Arc', 'Jesus', 'Joni', 'Leap of Faith', 'Left Behind', 'Left Behind', 'Left Behind III', 'Like Dandelion Dust', 'Marjoe', 'Martin Luther', 'Megiddo', 'Heaven', 'Mohammad Rasoolollah', 'Noah', "Mrs. Worthington's Party", 'One Night with the King', 'Our Fathers', "Preacher's Kid", 'Princess of Rome', 'Risen', 'Soul Surfer', 'Sunday School Musical', 'The Gospel', 'Il vangelo secondo Matteo', 'The Greatest Story Ever Told', 'The Hiding Place', 'The Prince of Egypt', 'Jesus', 'Molke Soleiman', 'Time Changer', 'Maryam-e Moghaddas', 'Pedro Calungsod', 'Son of God', 'The Message', "Moms' Night Out", 'The Omega Code', 'The Passion of the Christ', "The Pirates Who Don't Do Anything", 'The Second Chance', 'The Secrets of Jonathan Sperry', 'The Song of Bernadette', 'The Story of Jacob and Joseph', 'The Ten Commandments', 'The Ten Commandments', 'The Ten Commandments', 'The Messiah', 'Unidentified', 'Left Behind II', 'War Room', 'When the Game Stands Tall', 'Young Abraham', 'Expelled', 'Little Boy', 'The Young Messiah', 'October Baby', 'Minutes in Heaven', 'The Other Side of Heaven', 'Seven Days in Utopia', 'The Visual Bible', 'To Save a Life', 'The Ultimate Gift', 'The Work and the Glory', 'Last Ounce of Courage', 'The Judas Project', 'Letters to God', 'The Identical', "Kirk Cameron's Saving Christmas", "God's Army", 'Last Ounce of Courage', 'Thérèse', 'Captive', "God's Not Dead 2", 'The Bible', 'Farouk Omar', ''], ['King of Kings', 'Les Misérables in Concert', 'The Ten Commandments', 'Jesus of Nazareth', 'Ben-Hur', 'The Song of Bernadette', 'The Sound of Music', 'The Night of the Hunter', "The Nun's Story", 'Black Narcissus', 'Intolerance', 'San Francisco', 'Friendly Persuasion', 'The King of Kings', 'Les misérables', 'The Hunchback of Notre Dame', 'Ben-Hur A Tale of the Christ', 'A Man for All Seasons', "The Razor's Edge", 'Quo Vadis', "Schindler's List", 'The Hunchback of Notre Dame', 'The Sign of the Cross', 'The Crucible', 'Les Misérables in Concert', 'Les Misérables', 'The Greatest Story Ever Told', "Gentleman's Agreement", 'Samson and Delilah', 'Going My Way', 'Les Misérables', 'Romero', 'Cabin in the Sky', 'The Miracle of Our Lady of Fatima', 'The Nativity Story', 'Madre Teresa', 'The Scarlet and the Black', 'Les Misérables', 'The Angel Wore Red', 'The Fugitive', 'Plymouth Adventure', 'The Big Trees', 'Mary, Mother of Jesus', 'Legend of the Candy Cane', 'Knights of the Round Table', 'The House of Rothschild', 'Sergeant York', 'Salome', 'Sister Act', 'Des hommes et des dieux', 'Rain', 'Solomon and Sheba', 'The Big Fisherman', 'Joseph', 'The Fourth Wise Man', 'The Mighty Macs', 'Joshua', 'The Bible', 'Francis of Assisi', 'Rasputin', 'The Last Days of Pompeii', 'Millions', 'The Emissary', 'Jesus', 'Mouse on the Mayflower', 'The Small Miracle', 'The Bible', ''], ['A Week Awa', 'Bethany Hamilton', 'Blue Miracl', 'The Shack', 'Come Sunda', 'God Calling', 'Fatima', 'Mary Magdalene', 'The Young Messia', 'Gifted Hands', 'Notes for My Son', 'Related Stories', 'Glee', "Kris Jenner Has Health Scare in 'The Kardashians' Season 2 Trailer", 'Best Fall Soup Recipes to Bookmark Now for When Cooler Temperatures Hit', 'God Bless the Broken Roa', 'The Resurrection of Gavin Stone', 'Nothing to Lose', 'Penguin Bloo', 'alk. Ride. Rodeo.', 'Veggie Tales in the House', 'Good Sa', 'Hearts', 'Riding Faith', 'Voices of Fir', 'Rock My Hear', 'Our Lady of San Juan, Four Centuries of Miracles', 'Dreamer', 'The Blind Sid', 'Trending Stories', 'Glee', "Kris Jenner Has Health Scare in 'The Kardashians' Season 2 Trailer", 'Best Fall Soup Recipes to Bookmark Now for When Cooler Temperatures Hit', 'Drew Barrymore Blooms in Must-See Floral Couture Gown', 'Do Any of These Sound Familiar? 12 Signs You’re in a Situationship', '', "Henry Golding on Making Jane Austen's 'Persuasion' More Accessible", 'The 15 Best Patriotic Movies to Watch This Fourth of July Weekend', "Who's Left? The Complete List of Hallmark Channel Stars Who Are Not Leaving the Network", 'Hallmark Kicks Off Christmas Crazy Early With My Grownup Christmas List', "We're Going Back to the Future in 2023! New Musical Hits Broadway!", "A Reluctant Heir Sees the World Through a Caterer's Eyes in GAC Family's Catering Christmas"]]
good_count = 0
bad_count = 0
# for list in data:
#     for name in list:
#         res = give_movie_data(name)
#         print(name)
#         if res:
#             print('good')
#             good_count += 1
#         else:
#             print('bad!!!')
#             bad_count += 1

# print(good_count)
# print(bad_count)
print(give_movie_data('The Tree of Life'))