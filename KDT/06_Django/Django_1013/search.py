import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt.settings")
import django
django.setup()
import sys
import urllib.request

from movies.models import Movie

client_id = "IPhUkVIAszv7xBR4mppj" # 개발자센터에서 발급받은 Client ID 값
client_secret = "4EdSxFTI3A" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("해리포터")
url = "https://openapi.naver.com/v1/search/movie?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_dict = json.loads(response_body.decode('utf-8'))
    items = response_dict['items']
    for item in items:
        title = item['title'].replace('<b>', '').replace('</b>', '')
        image = item['image']
        Movie(title=title, content='test', image=image).save()
else:
    print("Error Code:" + rescode)