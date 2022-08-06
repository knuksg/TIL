x = int(input())
n = int(input())
rst = 0
for i in range(n):
    a, b = map(int, input().split())
    rst += a*b
if x == rst:
    print('Yes')
else:
    print('No')