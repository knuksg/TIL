t = int(input())
rst = list(range(t))
for i in range(t):
    a, b = map(int, input().split())
    rst[i] = a + b
for i in range(t):
    print(rst[i])