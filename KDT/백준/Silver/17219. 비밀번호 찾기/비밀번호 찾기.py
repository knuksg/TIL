n, m = map(int, input().split())
dic_ = {}
for _ in range(n):
    id, password = input().split()
    dic_[id] = password
for _ in range(m):
    site = input()
    print(dic_[site])