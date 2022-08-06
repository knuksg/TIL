n = list(input())
number = []
for i in range(len(n)):
    number.append(int(n[i]))
number = sorted(number)
for i in range(len(number)-1,-1,-1):
    print(number[i], end='')