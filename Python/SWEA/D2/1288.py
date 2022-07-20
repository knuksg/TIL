t = int(input())

for i in range(t):
    n = int(input())
    m = [n]
    cnt = 0
    result = set()
    while len(result) < 10:
        n = m[0]*(cnt)
        while n != 0:
            result.add(n%10)
            n = n//10
        cnt += 1
    n = m[0]*(cnt-1)
    print(f'#{i+1} {n}')
    cnt = 0
    result.clear()
    m.clear()