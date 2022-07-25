t = int(input())

for i in range(t):
    n = int(input())
    rst = 0
    for ii in range(1, n+1):
        if ii % 2 == 0:
            rst -= ii
        else:
            rst += ii
    print(f'#{i+1} {rst}')