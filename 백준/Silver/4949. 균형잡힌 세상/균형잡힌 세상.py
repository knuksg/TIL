while True:
    left_ = []
    answer = ''
    w = list(input())
    if w == ['.']:
        exit(0)
    for i in range(len(w)):
        if w[i] == ']' and not len(left_):
            answer = 'no'
            break
        elif w[i] == ')' and not len(left_):
            answer = 'no'
            break
        elif w[i] == ')' and left_[-1] == '[':
            answer = 'no'
            break
        elif w[i] == ']' and left_[-1] == '(':
            answer = 'no'
            break
        elif w[i] == '(':
            left_.append(w[i])
        elif w[i] == '[':
            left_.append(w[i])
        elif w[i] == ')':
            left_.pop()
        elif w[i] == ']':
            left_.pop()
    if answer == 'no' or len(left_):
        print('no')
    else:
        print('yes')