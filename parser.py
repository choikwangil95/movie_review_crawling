import requests
from bs4 import BeautifulSoup
## 아래 4줄을 추가해 줍니다.

import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "liontask.settings")

## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from crawl.models import Moviedata
location = 'https://movie.naver.com/movie/point/af/list.nhn?target=after&page='
    
def parse_movie(url):
    movies = []
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    target = table.find_all('tr')

    for n in range(1, 10):
        movie = {}

        title = target[n].find(class_='title').find('a').text.strip()
        movie['title'] = title
        review = target[n].find(class_='title').get_text()
        movie['review'] = review

        movies.append(movie)


    for m in movies:
        Moviedata(
            title = m['title'],
            review = m['review'],
        ).save()

for i in range(100):
    parse_movie(location+str(i))