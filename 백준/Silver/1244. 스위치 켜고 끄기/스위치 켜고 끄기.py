n = int(input())
number_list = list(map(int, input().split()))
s = int(input())
for _ in range(s):
    gender, number = map(int, input().split())
    # 남자일 떄
    if gender == 1:
        # 1이면 모든 스위치 반전
        if number == 1:
            for i in range(len(number_list)):
                number_list[i] = abs(number_list[i]-1)
        # 아니라면 스위치 번호가 주어진 번호의 배수일 때만 스위치 반전
        else:
            for i in range(len(number_list)):
                if (i+1) % number == 0:
                    number_list[i] = abs(number_list[i]-1)
    else:
        # 여자일 떄
        cnt = 0
        while True:
            cnt += 1
            if not(-1 < ((number-1) - cnt) and ((number-1) + cnt) < n):
                break
            if not(number_list[(number-1) - cnt] == number_list[(number-1) + cnt]):
                break
        cnt -= 1
        for i in range((number-1)-cnt, number+cnt):
            number_list[i] = abs(number_list[i]-1)
# 20개까지 나타내고 개행하기
for i in range(len(number_list)):
    print(number_list[i], end=' ')
    if (i+1)%20==0:
        print()