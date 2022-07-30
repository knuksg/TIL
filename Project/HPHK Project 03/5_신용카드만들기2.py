import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
for i in range(t):
    test_case = list(input())
    cnt = 0
    for j in range(len(test_case)):
        # 첫 숫자가 조건 충족하지 못하면 0 입력하고 브레이크.
        if j == 0 and test_case[j] not in ['3', '4', '5', '6', '9']:
            print(f'#{i+1} 0')
            break
        elif test_case[j] == '-':
            cnt = cnt
        # 숫자마다 카운트
        else:
            cnt += 1
    # 16자리일 때 1 출력, 아닐 때는 0 출력.
    if cnt == 16:
        print(f'#{i+1} 1')
    elif 0 < cnt :
        print(f'#{i+1} 0')
    else:
        continue