x = int(input())
rst = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    rst += a * b
if x == rst:
    print('Yes')
else:
    print('No')