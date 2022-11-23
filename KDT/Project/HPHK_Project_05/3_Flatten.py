import sys

sys.stdin = open("_Flatten.txt")

'''
가장 높은 지점 -1, 가장 낮은 지점 +1
정렬
이 과정을 반복하면 된다.
'''

for i in range(10):
    n = int(input())
    number = list(map(int, input().split()))
    sorted_number = sorted(number)
    for j in range(n):
        sorted_number[-1] -= 1
        sorted_number[0] += 1
        sorted_number = sorted(sorted_number)
    print(f'#{i+1} {max(sorted_number)-min(sorted_number)}')