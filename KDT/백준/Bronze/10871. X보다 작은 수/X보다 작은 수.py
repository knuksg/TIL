n, x = map(int, input().split())
m = list(map(int, input().split()))
for i in m:
    if i < x:
        print(i, end=' ')