while True:
    a, b, c = map(int, input().split())
    if not(a+b+c):
        break
    n = sorted([a, b, c])
    if n[0]**2+n[1]**2 == n[2]**2:
        print('right')
    else:
        print('wrong')