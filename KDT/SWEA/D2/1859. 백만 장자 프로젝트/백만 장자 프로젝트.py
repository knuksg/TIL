t = int(input())
for i in range(t):
    day = int(input())
    n = list(map(int, input().split()))
    rst = 0
    max1 = 0
    for j in reversed(range(day)):
        if n[j] > max1:
            max1 = n[j]
        else:
            rst += max1 - n[j]
    print(f'#{i+1} {rst}')