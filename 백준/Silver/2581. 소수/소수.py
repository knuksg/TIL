def sosu(n):
    sosu = True
    if n == 1:
        sosu = False
    else:
        for i in range(2, n):
            if n % i == 0:
                sosu = False
    return sosu

m = int(input())
n = int(input())
sosu_list = []
for i in range(m, n+1):
    if sosu(i) == True:
        sosu_list.append(i)
if not len(sosu_list):
    print(-1)
else:
    print(sum(sosu_list), min(sosu_list), sep='\n')