n = int(input())
cnt = 1
for i in range(1, n+1):
    cnt *= i
rst = 0
for i in range(len(str(cnt))-1,-1,-1):
    if str(cnt)[i] == '0':
        rst += 1
    else:
        break
print(rst)