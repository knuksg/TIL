import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())
for i in range(t):
    test_case = list(map(int, input().split()))
    test_dic = {}
    # 딕셔너리에 넣기.
    for j in test_case:
        test_dic[j] = test_dic.get(j, 0) + 1
    # 홀로 있는 수가 있다면 그 수 출력하기.
    for j in test_dic:
        if test_dic[j] == 1:
            print(f'#{i+1} {j}')
            break
    # 다 같은 수라면 그 수 출력하기.
    else:
        print(f'#{i+1} {j}')