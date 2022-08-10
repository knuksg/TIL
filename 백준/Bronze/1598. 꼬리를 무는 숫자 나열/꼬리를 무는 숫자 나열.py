a, b = map(int, input().split())
height = [1, 4, 3, 2]
a_h = height[a%4]
b_h = height[b%4]
if a % 4 == 0:
    a_w = a//4
else:
    a_w = a//4+1
if b % 4 == 0:
    b_w = b//4
else:
    b_w = b//4+1

print(abs(b_h-a_h)+abs(b_w-a_w))