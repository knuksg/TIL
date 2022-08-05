import sys

sys.stdin = open("_괄호짝짓기.txt")

bracket = ['(', '[', '{', '<', ')', ']', '}', '>']
for t in range(1, 11):
    bracket_list_len = int(input())
    bracket_list = list(input())
    left_ = []
    result = True
    for elem in bracket_list:
        # 왼쪽 괄호면 추가.
        if elem in bracket[0:4]:
            left_.append(elem)
        # 오른쪽 괄호인데 왼쪽 괄호 리스트가 비었으면 브레이크.
        elif elem in bracket[4:8] and not len(left_):
            result = False
            break
        # 오른쪽 괄호인데 상응하는 왼쪽 괄호가 아니면 브레이크.
        elif elem == bracket[4] and left_[-1] != bracket[0]:
            result = False
            break
        elif elem == bracket[5] and left_[-1] != bracket[1]:
            result = False
            break
        elif elem == bracket[6] and left_[-1] != bracket[2]:
            result = False
            break
        elif elem == bracket[7] and left_[-1] != bracket[3]:
            result = False
            break
        # 오른쪽 괄호인데 상응하는 왼쪽 괄호면 pop().
        else:
            left_.pop()
    print(f'#{t}' , end=' ')
    # 중간에 브레이크 없이 끝까지 True이면서, 
    # 왼쪽 괄호 리스트에 아무것도 안 남았을 경우에만 1 출력.
    if result == True and not len(left_):
        print(1)
    else:
        print(0)