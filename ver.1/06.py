import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    base = 'https://api.themoviedb.org/3'
    API_Key = os.getenv('API_Key')
    url1 = f'{base}/search/movie?api_key={API_Key}&language=ko-KR&query={title}&region=KR'
    response1 = requests.get(url1).json()
    
    try: # 실패할 경우-try, except 사용
        movie_id = response1.get('results')[0].get('id') # movie_id 줄은 try, except 밖에 나가면 indexerror생김
        url2 = f'{base}/movie/{movie_id}/credits?api_key={API_Key}&language=ko-KR&region=KR'
        response2 = requests.get(url2).json()
        credit_dict = {
            'cast': [],
            'crew': []
        }
        for cast in response2['cast']:
            if cast['cast_id'] < 10:
                credit_dict['cast'].append(cast['name'])
                
        for crew in response2['crew']:
            if crew['department'] == 'Directing':
                credit_dict['crew'].append(crew['name'])
        return credit_dict
        
    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
