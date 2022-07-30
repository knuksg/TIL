import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input())
for i in range(t):
    n = input()
    numbers = list(map(int, input().split()))
    numbers_dic = {}
    # 딕셔너리에 넣어 빈도수 세기.
    for i in numbers:
        numbers_dic[i] = numbers_dic.get(i, 0) + 1
    # 빈도수와 사전순으로 정렬하고 제일 뒤(높은) 숫자 꺼내기.
    print(f'#{n} {sorted(numbers_dic.items(), key=lambda x:(x[1], x[0]))[-1][0]}')