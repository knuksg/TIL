from collections import deque
n = int(input())
real_number = deque(list(map(int, input().split())))
m = int(input())
numbers = []
cnt = 0
for _ in range(m):
	first_number = list(map(int, input().split()))
	number = deque(first_number)
	reversed_number = deque([])
	for r in range(n-1,-1,-1):
		if number[r] == 1:
			reversed_number.append(3)
		elif number[r] == 2:
			reversed_number.append(4)
		elif number[r] == 3:
			reversed_number.append(1)
		elif number[r] == 4:
			reversed_number.append(2)
	for i in range(n):
		if number == real_number or reversed_number == real_number:
			numbers.append(first_number)
			cnt += 1
			break
		number.append(number.popleft())
		reversed_number.append(reversed_number.popleft())
print(cnt)
for number in numbers:
	print(*number)