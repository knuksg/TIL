def sosu(n):
    answer = 'YES'
    for i in range(2, n):
        if n % i == 0:
            answer = 'NO'
    return answer
n = int(input())
number = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if number[i] != 1 and sosu(number[i]) == 'YES':
        cnt += 1
print(cnt)