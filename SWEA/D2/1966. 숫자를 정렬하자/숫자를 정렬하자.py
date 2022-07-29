t = int(input())
for i in range(t):
    n = int(input())
    rst = sorted(list(map(int, input().split())))
    print(f'#{i+1}', end=' ')
    for i in range(n):
        if i != n-1:
            print(rst[i], end=' ')
        else:
            print(rst[i])