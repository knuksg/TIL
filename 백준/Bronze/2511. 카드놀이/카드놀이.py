A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_cnt = 0 # A의 점수.
B_cnt = 0 # B의 점수.
win_list = [] # 매 판마다 누가 이겼는지 기록.
for i in range(10):
    if A[i] > B[i]:
        A_cnt += 3
        win_list.append('A')
    elif A[i] == B[i]:
        A_cnt += 1
        B_cnt += 1
        win_list.append('D')
    else:
        B_cnt += 3
        win_list.append('B')
print(A_cnt, B_cnt) # A와 B의 총점 프린트.
if A_cnt > B_cnt:
    print('A')
elif B_cnt > A_cnt:
    print('B')
else: # 총점이 같을 경우
    for i in range(-1, -len(win_list), -1):
        # 매판 승리 기록을 뒤에서부터 보는데, D가 아니면 출력하고 브레이크.
        if win_list[i] != 'D':
            print(win_list[i])
            break
    else:
        print('D')