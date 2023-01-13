import requests
import os
from dotenv import load_dotenv
load_dotenv()

def popular_count():
    pass 
    # 여기에 코드를 작성합니다. 
    base = 'https://api.themoviedb.org/3'
    API_Key = os.getenv('API_Key')
    url = f'{base}/movie/popular?api_key={API_Key}&language=ko-KR&region=KR'
    response = requests.get(url).json()
    return len(response.get('results'))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
