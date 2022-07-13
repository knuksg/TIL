a, m, d, n = map(int, input().split())
rst = a
cnt = 0
while cnt < n -1:
    cnt += 1
    rst = rst * m + d
print(rst)