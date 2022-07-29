import json
from pprint import pprint


def movie_info(movie):
    f = open('data/movie.json', 'r', encoding='utf-8')
    mv = json.load(f)
    return  {
        'genre_ids' : mv.get('genre_ids'),
        'id' : mv.get('id'),
        'overview' : mv.get('overview'),
        'title' : mv.get('title'),
        'vote_average' : mv.get('vote_average')
        }
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))