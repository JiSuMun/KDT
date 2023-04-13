import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    base = 'https://api.themoviedb.org/3'
    API_Key = os.getenv('API_Key')
    url1 = f'{base}/search/movie?api_key={API_Key}&language=ko-KR&query={title}&region=KR'
    response1 = requests.get(url1).json()
    

    try: # 실패할 경우-try, except 사용
        movie_id = response1.get('results')[0].get('id') # movie_id 줄은 try, except 밖에 나가면 indexerror생김
        url2 = f'{base}/movie/{movie_id}/recommendations?api_key={API_Key}&language=ko-KR&region=KR'
        response2 = requests.get(url2).json()
        recommend_movies = []

        for movie in response2.get('results'):
            recommend_movies.append(movie['title'])
        return recommend_movies
    except:
        return None

    
    
        
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
