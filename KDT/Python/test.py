# import sys
# input = sys.stdin.readline
from collections import deque
import heapq
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
number_list = list(map(int, input().split()))
s = int(input())
for _ in range(s):
    gender, number = map(int, input().split())
    # 남자일 떄
    if gender == 1:
        # 1이면 모든 스위치 반전
        if number == 1:
            for i in range(len(number_list)):
                number_list[i] = abs(number_list[i]-1)
        # 아니라면 
        else:
            for i in range(len(number_list)):
                if (i+1) % number == 0:
                    number_list[i] = abs(number_list[i]-1)
    else:
        cnt = min(number-1, n-number)
        for i in range((number-1)-cnt, (number)+cnt):
            number_list[i] = abs(number_list[i]-1)
for i in range(len(number_list)):
    print(number_list[i], end=' ')
    if (i+1)%20==0:
        print()