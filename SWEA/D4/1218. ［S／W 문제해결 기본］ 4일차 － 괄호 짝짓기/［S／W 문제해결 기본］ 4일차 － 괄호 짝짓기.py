bracket = ['(', '[', '{', '<', ')', ']', '}', '>']
for t in range(1, 11):
    bracket_list_len = int(input())
    bracket_list = list(input())
    left_ = []
    result = True
    for elem in bracket_list:
        if elem in bracket[0:4]:
            left_.append(elem)
        elif elem in bracket[4:8] and not len(left_):
            result = False
            break
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
        else:
            left_.pop()
    print(f'#{t}' , end=' ')
    if result == True and not len(left_):
        print(1)
    else:
        print(0)