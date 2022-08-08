for _ in range(int(input())):
    rst = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        rst += str(i).count('0')
    print(rst)