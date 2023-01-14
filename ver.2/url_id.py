import requests

class URL():
    BASE_URL = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key
        
    def get_url(self, path, **kwargs):
        url = f'{URL.BASE_URL}{path}?api_key={self.key}'

        for key, value in kwargs.items():
            url += f'&{key}={value}'
        
        return url
    
    def movie_id(self, title):

        url = self.get_url('/search/movie', language='ko-KR', region = 'KR', query = title)

        response = requests.get(url).json()
        if response.get('results'):
            id = response.get('results')[0].get('id')
            return id
        else:
            return None
