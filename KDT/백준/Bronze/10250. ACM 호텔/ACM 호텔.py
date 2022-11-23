for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h != 0:
        rst1 = n // h + 1
        rst2 = n % h
    else:
        rst1 = n // h
        rst2 = h
    if rst1 < 10:
        print(rst2, rst1, sep='0')
    else:
        print(rst2, rst1, sep='')