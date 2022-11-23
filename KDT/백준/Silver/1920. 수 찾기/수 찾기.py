set_ = set()
n = int(input())
list_ = input().split()
for i in range(n):
    set_.add(list_[i])
m = int(input())
list_m = input().split()
for i in range(m):
    if list_m[i] in set_:
        print(1)
    else:
        print(0)