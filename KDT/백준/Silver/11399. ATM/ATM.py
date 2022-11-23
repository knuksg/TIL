n = int(input())
number = list(map(int, input().split()))
number = sorted(number)
cnt = 0
for i in range(len(number)):
    cnt += number[i] * (len(number)-i)
print(cnt)