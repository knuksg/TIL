reward1 = [0]+[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6
reward2 = [0]+[512]+[256]*2+[128]*4+[64]*8+[32]*16

for _ in range(int(input())):
    win_reward = 0
    a, b = map(int, input().split())
    if a > 21:
        a = 0
    else:
        win_reward += reward1[a]
    if b > 31:
        b = 0
    else:
        win_reward += reward2[b]
    if win_reward != 0:
        print(win_reward, '0000', sep='')
    else:
        print(0)