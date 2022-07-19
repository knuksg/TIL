t = int(input())

for i in range(t):
    n = map(int, input().split())
    m = list(n)
    rst = 0
    for ii in m:
        if ii % 2 != 0:
            rst += ii
    print(f'#{i+1} {rst}')
    rst = 0