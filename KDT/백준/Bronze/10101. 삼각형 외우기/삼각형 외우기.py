a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == 60 and c == 60:
    print('Equilateral')
elif a + b + c == 180:
    if a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')