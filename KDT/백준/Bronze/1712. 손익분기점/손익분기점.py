a, b, c = map(int, input().split())
cnt = -1
if b < c:
    cnt = 1
    cnt += a//(c-b)
print(cnt)