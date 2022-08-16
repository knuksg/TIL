import sys

sys.stdin = open("_퍼펙트셔플.txt")

'''
짝수면 둘로 나누고 차례차례 출력한다.
홀수면 앞 그룹에 하나 더 주고 나눈 뒤 차례차례 출력한다.
'''


for i in range(int(input())):
    n = int(input())
    word = input().split()
    if n % 2 == 0:
        word1 = word[0:n//2]
        word2 = word[n//2:]
        print(f'#{i+1}', end=' ')
        for i in range(n//2):
            print(word1[i], end=' ')
            print(word2[i], end=' ')
        print()
    else:
        word1 = word[0:n//2+1]
        word2 = word[n//2+1:]
        print(f'#{i+1}', end=' ')
        for i in range(n//2+1):
            if i == n//2:
                print(word1[i], end=' ')
                continue
            print(word1[i], end=' ')
            print(word2[i], end=' ')
        print()