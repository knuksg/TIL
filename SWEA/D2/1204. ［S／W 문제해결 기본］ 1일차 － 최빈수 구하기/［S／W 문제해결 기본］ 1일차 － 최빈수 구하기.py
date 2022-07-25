t = int(input())
for i in range(t):
    a = input()
    rst = {}
    numbers = map(int, input().split())
    for ii in numbers:
        rst[ii] = rst.get(ii, 0) + 1
    print(f'#{a} {sorted(rst.items(), key=lambda x:(x[1], x[0]))[-1][0]}')