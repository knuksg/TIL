n = input()
def baesu(n:str, cnt = 1):
    x = sum(map(int, list(n)))
    if  x >= 10:
        return baesu(str(x), cnt+1)
    else:
        if x % 3 == 0:
            print(cnt)
            print('YES')

        else:
            print(cnt)
            print('NO')
if int(n) >= 10:
    baesu(n)
else:
    print(0)
    if int(n)%3 == 0:
        print('YES')
    else:
        print('NO')