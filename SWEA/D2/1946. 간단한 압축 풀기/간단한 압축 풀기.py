t = int(input())
for i in range(t):
    print(f'#{i+1}')
    N = int(input())
    rst = ''
    for ii in range(N):
        a, b = input().split()
        rst += a*int(b)
    for j in range(1, len(rst)+1):
        if j % 10 == 0 or j == len(rst):
            print(rst[j-1], end='\n')
        else:
            print(rst[j-1], end='')