from collections import deque
number = []

for a in range(1,10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				list_ = deque([])
				list_.append((a))
				list_.append((b))
				list_.append((c))
				list_.append((d))
				list_list = []
				for _ in range(4):
					list_list.append(list_[0]*1000+list_[1]*100+list_[2]*10+list_[3])
					list_.append(list_.popleft())
				new_number = min(list_list)
				if new_number in number:
					continue
				number.append(new_number)
list_2 = deque(list(map(int, input().split())))
list_list2 = []
for _ in range(4):
	list_list2.append(list_2[0]*1000+list_2[1]*100+list_2[2]*10+list_2[3])
	list_2.append(list_2.popleft())
new_number2 = min(list_list2)

for i in range(len(number)):
	if number[i] == new_number2:
		print(i+1)