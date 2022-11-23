n, k = map(int, input().split())
number = list(map(int, input().split()))
print(sorted(number)[k-1])