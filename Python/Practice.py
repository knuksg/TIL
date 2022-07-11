from re import X


x, y = 10, 20
print(x, y)
y, x = x, y
print(x, y)

tmp = x
x = y
y = tmp
print(x, y)
