import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = list(map(int, str(a*b*c)))
rst = {}
for i in d:
    rst[i] = rst.get(i, 0) + 1
for i in range(10):
    if rst.get(i) == None:
        print(0)
    else:
        print(rst[i])