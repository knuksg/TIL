t = int(input())

for i in range(t):
    n = map(int, input().split())
    rst = 0
    cnt = 0
    for ii in n:
        rst += ii
        cnt += 1
    print(f'#{i+1} {rst/cnt:.0f}')
    rst = 0
    cnt = 0