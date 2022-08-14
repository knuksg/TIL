list_ = []
n, k = map(int, input().split())
for _ in range(n):
    list_.append(int(input()))
cnt = 0
while k:
    for i in range(n-1, -1, -1):
        if k >= list_[i]:
            cnt += k//list_[i]
            k = k%list_[i]
print(cnt)