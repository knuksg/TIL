import json
from pprint import pprint

def movie_info(movie, genres):

    result = []
    for x in range(len(movie)):
        genre_names = []
        for i in range(len(movie[x].get('genre_ids'))):
            for ii in range(len(genres)):
                if movie[x].get('genre_ids')[i] == genres[ii].get('id'):
                    genre_names.append(genres[ii].get('name'))
        result.append({
        'genre_names' : genre_names,
        'id' : movie[x].get('id'),
        'overview' : movie[x].get('overview'),
        'title' : movie[x].get('title'),
        'vote_average' : movie[x].get('vote_average')
        })
    result.sort(reverse=True, key=lambda result : result['vote_average'])
    return  result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))