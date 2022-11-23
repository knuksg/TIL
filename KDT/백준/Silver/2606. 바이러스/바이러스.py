n = int(input())
m = int(input())
com = [[]*(n) for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    com[u-1].append(v)
    com[v-1].append(u)

list_ = [1]
rst = []

while list_:
    if list_[-1] not in rst:
        rst.append(list_.pop())
    else:
        list_.pop()
    for i in com[rst[-1]-1]:
        if i not in rst:
            list_.append(i)
print(len(rst)-1)