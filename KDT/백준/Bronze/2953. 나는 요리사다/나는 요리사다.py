cook = {}
for i in range(1, 6):
    cook[i] = sum(map(int, input().split()))
winner = list(sorted(cook.items(), key=lambda x:x[1])[-1])
print(winner[0], winner[1])