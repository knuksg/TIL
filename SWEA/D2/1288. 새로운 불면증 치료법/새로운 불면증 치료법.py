t = int(input())
for i in range(t):
    n = int(input())
    m = n
    result = set()
    while True:
        for j in str(n):
            result.add(j)
        if len(result) == 10:
            break
        n += m
    print(f'#{i+1} {n}')