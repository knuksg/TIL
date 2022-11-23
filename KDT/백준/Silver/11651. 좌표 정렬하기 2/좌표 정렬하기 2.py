n = int(input())
number = []
for i in range(n):
    number.append(list(map(int, input().split())))
number = sorted(number, key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*number[i])