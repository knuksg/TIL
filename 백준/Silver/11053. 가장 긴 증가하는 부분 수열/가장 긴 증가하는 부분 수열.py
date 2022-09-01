n = int(input())
number = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    list_ = []
    for j in range(1, i+1):
        if number[j-1] < number[i]:
            list_.append(dp[j-1])
    if list_:
        dp[i] = max(list_)+1
print(max(dp))