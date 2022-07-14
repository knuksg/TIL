# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # for i in range(n):
# #     r = list(map(int, input().split()))
# #     print(f'Case #{i+1}: {r[0]} + {r[1]} = {r[0]+r[1]}', sep='')

# n = int(input())
# for i in range(1, n+1):
#     print((n-i)*' '+ '*'*i)

n, x = map(int, input().split())
m = list(map(int, input().split()))
for i in m:
    if i < x:
        print(i, end=' ')