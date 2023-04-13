import requests
from url_id import URL
import os
from dotenv import load_dotenv
load_dotenv()


def popular_count():
    pass
    # 여기에 코드를 작성합니다. 
    key = os.getenv('API_Key')
    url = URL(key).get_url('/movie/popular', region='KR', language='ko-KR')
    response = requests.get(url).json()
    return len(response.get('results'))
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20