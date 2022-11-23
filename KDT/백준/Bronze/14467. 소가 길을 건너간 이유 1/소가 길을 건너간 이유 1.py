n = int(input())
cow = {}
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if cow.get(a) == None:
        cow[a] = b+1
    elif cow.get(a) != b+1:
        cow[a] = b+1
        cnt += 1
print(cnt)