from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    context = {
        'name': '김선교',
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request,'index.html', context)

def welcome(reqeust, name):
    # 사람들이 /welcome/본인 이름을 입력하면 환영 인사와 이름을 동시에 보여준다.
    context = {
        'name': name,
    }
    return render(reqeust, 'welcome.html', context)