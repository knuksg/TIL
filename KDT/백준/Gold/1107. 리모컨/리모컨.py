from collections import deque

# 이동하려고 하는 채널
n = int(input())

# 고장난 버튼의 개수
m = int(input())

# 고장난 버튼의 개수가 0이 아니라면
if m != 0:
    # 고장난 버튼의 집합과 다른 숫자 집합의 교집합을 구하기 위해 세트에 넣는다.
    broken = set(input().split())
    deq = deque()

    # 이동하려는 채널이 100번 이상일 때
    if n >= 100:
        for i in range(100, 1000001):

            # 고장난 버튼이 없는 숫자들 중에서
            if len(set(list(str(i))) & broken) == 0:
                # (i와 n의 차이, i)를 덱에 넣는다.
                deq.append((abs(i-n), i))

    # 100번 미만일 떄
    else:
        for i in range(100):
            # 고장난 버튼이 없는 숫자들 중에서
            if len(set(list(str(i))) & broken) == 0:
                # (i와 n의 차이, i)를 덱에 넣는다.
                deq.append((abs(i-n), i))

    # 덱이 있으면
    if deq:

        # n과 가장 가까운 숫자를 min_ 변수에 넣는다.
        min_ = min(deq)

        # n과 min_의 차이 + min_의 길이가 100에서 시작해서 +/- 버튼을 누르는 것보다 작다면
        if abs(n-min_[1])+len(str(min_[1])) < abs(n-100):
            # n과 min_의 차이 + min_의 길이를 출력한다.
            print(abs(n-min_[1]) + len(str(min_[1])))

        # 102의 경우 +1 +1 (2회), 1/0/2 (3회)
        # 103의 경우 +1 +1 +1 (3회), 1/0/3 (3회)
        # 104의 경우 +1 +1 +1 +1 (4회), 1/0/4 (3회)
        
        # 그렇지 않다면
        else:
            # n과 100의 차이를 출력한다.
            print(abs(n-100))
    
    # 덱이 없으면
    else:
        print(abs(n-100))

# 고장난 버튼이 없으면
else:
    if abs(n-100) > len(str(n)):
        print(len(str(n)))
    else:
        print(abs(n-100))