n = int(input())
number = []
for i in range(n):
    number.append(list(map(int, input().split())))
number = sorted(number)
for i in range(n):
    print(*number[i])