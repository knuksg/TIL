n, k = map(int, input().split())
number = list(map(int, input().split()))
cnt = 0
max_cnt = 0
for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            cnt = number[x] + number[y] + number[z]
            if k >= cnt and cnt > max_cnt:
                max_cnt = cnt
print(max_cnt)