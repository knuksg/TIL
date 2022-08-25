n, k = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number)
print(number[-k])