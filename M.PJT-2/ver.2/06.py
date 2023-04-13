import requests
from pprint import pprint
from url_id import URL
import os
from dotenv import load_dotenv
load_dotenv()


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    
    try:
    
        key = os.getenv('API_Key')
        movie_id = URL(key).movie_id(title)
        url = URL(key).get_url(f'/movie/{movie_id}/credits', region='KR', language='ko-KR')
        response = requests.get(url).json()
        credit_dict = {
            'cast': [],
            'crew': []
        }
        for cast in response['cast']:
                if cast['cast_id'] < 10:
                    credit_dict['cast'].append(cast['name'])
                    
        for crew in response['crew']:
            if crew['department'] == 'Directing':
                credit_dict['crew'].append(crew['name'])

        return credit_dict
    except:
        None



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
