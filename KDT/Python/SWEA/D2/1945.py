t = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(t):
    n = int(input())
    while n%2==0:
        a += 1
        n /= 2
    while n%3==0:
        b += 1
        n /= 3
    while n%5==0:
        c += 1
        n /= 5
    while n%7==0:
        d += 1
        n /= 7
    while n%11==0:
        e += 1
        n /= 11
    print(f'#{i+1} {a} {b} {c} {d} {e}')
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0