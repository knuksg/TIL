fibonacci = [0]*41
fibonacci[0] = 0
fibonacci[1] = 1
for i in range(2, 41):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(fibonacci[n-1], fibonacci[n])