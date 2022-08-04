for _ in range(int(input())):
    arr = list(input().split())
    for elem in arr:
        print(*list(reversed(elem)), sep='', end=' ')
    print()