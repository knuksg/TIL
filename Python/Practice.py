x, y = 10, 20
print(x, y)
y, x = x, y
print(x, y)

tmp = x
x = y
y = tmp
print(x, y)


a = int(input())
if a > 150:
    print('매우 나쁨')
elif a > 80:
    print('나쁨')
elif a > 30:
    print('보통')
else:
    print('좋음')

n = 0
result = 0
user_input = int(input())
while user_input > n:
    n += 1
    result += n
print(result)