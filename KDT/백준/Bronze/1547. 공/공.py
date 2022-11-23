m = int(input())
cup = '123'
for i in range(m):
    a, b = input().split()
    tem = '@'
    cup1 = cup.replace(a, tem)
    cup2 = cup1.replace(b, a)
    cup = cup2.replace(tem, b)
print(cup[0])