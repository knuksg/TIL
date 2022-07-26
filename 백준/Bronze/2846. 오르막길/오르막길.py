n = int(input())
gil = list(map(int, input().split()))
cnt = 0
rst = []
for i in range(len(gil)-1):
    if gil[i+1] > gil[i]:
        cnt += gil[i+1] - gil[i]
    else:
        rst.append(cnt)
        cnt = 0
rst.append(cnt)
print(max(rst))