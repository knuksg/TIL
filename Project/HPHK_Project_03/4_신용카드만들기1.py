import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())
for i in range(t):
    test_case = list(map(int, input().split()))
    cnt = 0
    # 홀수면 *2 후 더하고, 짝수면 그냥 더하기.
    for j in range(len(test_case)):
        if j % 2 == 0:
            cnt += test_case[j]*2
        else:
            cnt += test_case[j]
    # 10으로 나눈 나머지에다 얼마를 더해야 10이 될지 계산하기.
    rst = 10 - (cnt % 10)
    # cnt가 0, 즉 딱 떨어질 때는 rst가 10이 되니까 0 출력, 이외에는 rst 출력하기.
    if rst != 10:
        print(f'#{i+1} {rst}')
    else:
        print(f'#{i+1} 0')