x, y, w, h = map(int, input().split())
xcnt = min(x, w-x)
ycnt = min(y, h-y)
print(min(xcnt, ycnt))