T = int(input())
for i in range(T):
    a, b = input().split()
    print(*map(lambda n:n*int(a), list(b)), sep='')