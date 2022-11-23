import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())
for i in range(t):
    n = int(input())
    test_case = list(map(int, input().split()))
    # 평균 구하기.
    center = sum(test_case)/n
    rst = 0
    # 평균보다 작으면 카운트하기.
    for j in range(n):
        if test_case[j] <= center:
            rst += 1
    print(f'#{i+1} {rst}')