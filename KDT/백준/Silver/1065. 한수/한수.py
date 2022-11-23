number = int(input())

def hansu(n):
    a = list(map(int, str(n)))
    b = set()
    if n < 100:
        return True
    else:
        for i in range(len(str(n))-1):
            b.add(a[i]-a[i+1])
        if len(b) == 1:
            return True
        else:
            return False

rst = 0
for i in range(1, number+1):
    if hansu(i) == True:
        rst += 1
print(rst)