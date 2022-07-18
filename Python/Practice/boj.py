# # import sys
# # input = sys.stdin.readline
# # n = int(input())
# # for i in range(n):
# #     r = list(map(int, input().split()))
# #     print(f'Case #{i+1}: {r[0]} + {r[1]} = {r[0]+r[1]}', sep='')
# m = list(map(int, input().split()))
# n = int(input())
# for i in range(1, n+1):
#     print((n-i)*' '+ '*'*i)

# 파이썬 런타임 에러 해결 (try-exept 구문)
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

# n = int(input())
# rst = n
# cnt = 0

# while True:
#     if n >= 10:
#         a = n%10*10
#         b = (n//10+n%10)%10
#         n = a + b
#     else:
#         a = n*10
#         b = n
#         n = a + b
#     if n != rst:
#         cnt += 1
#         continue
#     else:
#         cnt += 1
#         break
# print(cnt)

# n = int(input())
# m = list(map(int, input().split()))
# m.sort()
# print(m[0], m[-1])

# numbers = []
# while len(numbers) <= 8:
#     numbers.append(int(input()))
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max = i
# print(max)
# print(numbers.index(max)+1)

# a = int(input())
# b = int(input())
# c = int(input())
# d = list(map(int, str(a*b*c)))
# rst = {}
# for i in d:
#     rst[i] = rst.get(i, 0) + 1
# for i in range(10):
#     if rst.get(i) == None:
#         print(0)
#     else:
#         print(rst[i])

# ten = []
# while len(ten) <= 9:
#     ten.append(int(input())%42)
# print(len(set(ten)))

# n = int(input())
# m = list(map(int, input().split()))

# print(sum(m)/max(m)*100/n)


# a = int(input())
# m = []
# while len(m) < a:
#     m.append(list(input().strip()))
# cnt = 0
# score = 0
# scores = []
# for ii in range(len(m)):
#     for i in m[ii]:
#         if i == 'O':
#             score += (1+cnt)
#             cnt += 1
#         else:
#             cnt = 0
#     scores.append(score)
#     score = 0
#     cnt = 0
# for i in range(a):
#     print(scores[i])

import sys
input = sys.stdin.readline

c = int(input())
b = 0
ns = []
for i in range(c):
    n = map(int, input().split())
    ns = list(n)
    a = (sum(ns) - ns[0]) / ns[0] # 평균
    na = ns[0]
    del ns[0]
    for i in ns:
        if i > a:
            b += 1
    print(f'{b/na*100:.3f}%')
    b = 0