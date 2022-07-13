n = int(input())
m = 0
while n >= m:
    if m % 3 == 0:
        m += 1
    else:
        print(m, end=' ')
        m += 1