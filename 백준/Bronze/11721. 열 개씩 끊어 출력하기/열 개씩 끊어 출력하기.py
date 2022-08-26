w = input()
for i in range(len(w)):
	if i != 0 and i % 10 == 0:
		print()
	print(w[i], end='')