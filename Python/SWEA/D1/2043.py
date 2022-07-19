p, k = map(int, input().split())

while True:
    if p>k:
        print(p-k+1)
    else:
        print(999-k+p)
    break