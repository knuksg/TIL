import requests
from pprint import pprint

def credits(title):
    BASE_URL = f'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '5ddd1a3a8b4aeb5b2822e27f6b6231ef',
        'language': 'ko-KR',
        'query' : title
    }
    params2 = {
        'api_key': '5ddd1a3a8b4aeb5b2822e27f6b6231ef',
        'language': 'ko-KR'
    }
    try:
        response = requests.get(BASE_URL+path, params=params).json()
        movie_id = response.get('results')[0].get('id')
        path2 = '/movie/'+str(movie_id)+'/credits'
        response2 = requests.get(BASE_URL+path2, params=params2).json()
        cast1 = response2.get('cast')
        crew1 = response2.get('crew')
        cast = []
        crew = []
        rst = {'cast': cast, 'crew': crew}
        for i in cast1:
            if i.get('cast_id') < 10:
                cast.append(i.get('name'))
        for i in crew1:
            if i.get('department') == 'Directing':
                crew.append(i.get('name'))
        return rst
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
