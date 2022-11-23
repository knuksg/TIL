def self():
    a = list(range(1, 10000))
    m = 0
    for i in range(1, 10000):
        n = i
        while (i!=0):
            m += i%10
            i = i//10
        result = n + m
        if result < 10000:
            a[result-1] = 0
        m = 0
        result = 0
    for i in range(0, 9999):
        if a[i] == 0:
            continue
        print(a[i])

self()