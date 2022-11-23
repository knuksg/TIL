n = int(input())
cnt = 0
N = 0
for i in range(1, n+1):
    rst = i
    while i!=0:
        N = i%10
        i = i//10
        if N % 3 == 0 and N != 0:
            cnt += 1
    if cnt == 0:
        print(rst, end=' ')
    else:
        print('-'*cnt, end=' ')
    cnt = 0
    N = 0