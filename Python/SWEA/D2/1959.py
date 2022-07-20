t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    c = 0
    d = 0
    a = map(int, input().split())
    b = map(int, input().split())
    A = list(a)
    B = list(b)
    rst = []
    if n > m:
        c = n - m
        for i in range(m):
            for ii in range(c+1):
                rst.append(B[i]*A[ii])
        print(max(rst))
    else:
        c = m - n
        for i in range(n):
            for ii in range(c+1):
                rst.append(A[i]*B[ii])
        print(max(rst))
    n = 0
    m = 0
    a = 0
    b = 0
    A.clear()
    B.clear()
    rst.clear()