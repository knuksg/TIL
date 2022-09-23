from multiprocessing import context
import random
from django.shortcuts import render

# Create your views here.
# index 함수 선언 정의
def index(request):

    return render(request, 'index.html')

def template(request):
    number_list = [1,2,3,4,]

    context = {
        'numbers': number_list
    }
    return render(request, 'template.html', context)

def todaydinner(request):
    menu_list = ['볶음밥', '삼겹살', '부대찌개', '돈까스', '치킨', '떡볶이', '보쌈', '갈비찜', '초밥', ]
    img_list = [
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F63juJ%2Fbtrr0BsmSRL%2FXh4qVLOOBMVWw10vxKmyck%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbrtGvK%2FbtrrYS9uzB3%2FKFtxyLxmxjHCIqNkKyPpn0%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlIyM6%2FbtrrXMuYdc9%2FrxILVG0LjZq20otnSVCfHk%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdi4z12%2FbtrrVrdQp9G%2FOukII69ingTH6hX78d1gw0%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fevy733%2FbtrrVYv66Dl%2FJD7Zrgm5XXvUZsSfCW0qEk%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWFODO%2FbtrrW25SyQ2%2FMDN0vmUftXF6t1itbB9Go1%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqHR1I%2Fbtrr0QJEqq0%2FlmWeyZ4oooFmkCNmqlG6t1%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F0BRz7%2Fbtrr0BTxwSD%2FKS11WwJyjXiwjm0tnEUZJ0%2Fimg.png',
        'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlfIHd%2Fbtrr0so31oR%2FgQ1poUTbERDCpjMCBAeeqk%2Fimg.png',
    ]
    idx = random.choice(list(range(len(menu_list))))
    context = {
        'menu': menu_list[idx],
        'img': img_list[idx],
    }
    return render(request, 'todaydinner.html', context)

def lottery(request):
    numbers_list = ['', '', '', '', '']
    for i in range(5):
        numbers = random.sample(range(1, 46), 6)
        numbers = sorted(numbers)
        numbers_set = set()
        for number in numbers: 
            numbers_list[i] += str(number) + ' '
            numbers_set.add(number)
        if numbers_set == {3, 11, 15, 29, 35, 44}:
            numbers_list[i] = ['1등', numbers_list[i]]
        elif len(numbers_set & {3, 10, 11, 15, 29, 35, 44}) == 6:
            numbers_list[i] = ['2등', numbers_list[i]]
        elif len(numbers_set & {3, 11, 15, 29, 35, 44}) == 5:
            numbers_list[i] = ['3등', numbers_list[i]]
        elif len(numbers_set & {3, 11, 15, 29, 35, 44}) == 4:
            numbers_list[i] = ['4등', numbers_list[i]]
        elif len(numbers_set & {3, 11, 15, 29, 35, 44}) == 3:
            numbers_list[i] = ['5등', numbers_list[i]]
        else:
            numbers_list[i] = ['6등', numbers_list[i]]
    context = {
        'numbers': numbers_list,
    }
    return render(request, 'lottery.html', context)