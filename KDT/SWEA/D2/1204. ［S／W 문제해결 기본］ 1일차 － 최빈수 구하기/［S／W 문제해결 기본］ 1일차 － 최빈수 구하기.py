t = int(input())
for i in range(t):
    n = input()
    numbers = list(map(int, input().split()))
    numbers_dic = {}
    for i in numbers:
        numbers_dic[i] = numbers_dic.get(i, 0) + 1
    print(f'#{n} {sorted(numbers_dic.items(), key=lambda x:(x[1], x[0]))[-1][0]}')