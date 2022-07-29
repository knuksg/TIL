import requests

BASE_URL = f'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '5ddd1a3a8b4aeb5b2822e27f6b6231ef'
}
def popular_count():
    response = requests.get(BASE_URL+path, params=params).json()
    return len(response.get('results')) 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20