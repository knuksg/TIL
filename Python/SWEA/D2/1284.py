t = int(input())

for i in range(t):
    n = map(int, input().split())
    m = list(n)
    a = m[0]*m[4]
    b = 0
    if m[4] < m[2]:
        b = m[1]
    else:
        b = m[1]+m[3]*(m[4]-m[2])
    if a > b:
        print(f'#{i+1} {b}')
    else:
        print(f'#{i+1} {a}')