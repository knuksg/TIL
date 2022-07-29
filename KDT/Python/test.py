import sys
sys.stdin = open("input.txt", "r")

for i in range(10):
    n = int(input())
    test_case = list(input().split())
    c = int(input())
    c_list = input().split('I')
    command_list = []
    for j in range(c+1):
        if j != 0:
            command_list.append(c_list[j].split())
    for j in command_list:
        for x in range(int(j[1])):
            test_case.insert(int(j[0]), j[len(j)-x-1])
    print(f'#{i+1}', end=' ')
    for j in range(len(test_case)):
        if j == 9:
            print(test_case[j])
            break
        else:
            print(test_case[j], end=' ')