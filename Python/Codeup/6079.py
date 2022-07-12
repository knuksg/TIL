rst = int(input())
n = 0
a = 0
while True:
    if rst > n:
        a += 1
        n += a
    else:
        print(a)
        break