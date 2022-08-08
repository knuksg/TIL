for _ in range(int(input())): 
    s = int(input())
    n = int(input())
    rst = 0
    for i in range(n):
        q, p = map(int, input().split())
        rst += q*p
    print(s+rst)