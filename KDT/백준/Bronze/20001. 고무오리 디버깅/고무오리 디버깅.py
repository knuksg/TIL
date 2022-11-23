start = input()
duck = []
w = input()
while w != '고무오리 디버깅 끝':
    if w == '문제':
        duck.append(w)
    elif w == '고무오리' and len(duck) != 0:
        duck.pop()
    else:
        duck.append('문제')
        duck.append('문제')
    w = input()
if len(duck) != 0:
    print('힝구')
else:
    print('고무오리야 사랑해')