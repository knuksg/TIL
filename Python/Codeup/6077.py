n = int(input())
rst = 0
for i in range(n+1):
    if i % 2 == 0:
        rst += i
print(rst)