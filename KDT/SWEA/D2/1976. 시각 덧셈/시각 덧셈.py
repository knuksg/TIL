t = int(input())
for i in range(t):
    n = map(int, input().split())
    m = list(n)
    a = 0
    b = 0
    if m[1] + m[3] > 59:
        b = m[1] + m[3] - 60
        a += 1
    else:
        b = m[1] + m[3]
    if m[0] + m[2] > 12:
        a += m[0] + m[2] - 12
    else:
        a += m[0] + m[2]
    print(f'#{i+1} {a} {b}')