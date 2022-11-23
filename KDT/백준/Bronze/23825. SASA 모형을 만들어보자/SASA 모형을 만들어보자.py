N, M = map(int, input().split())
cnt = 0
if N > M:
    cnt = M
else:
    cnt = N
print(cnt//2)