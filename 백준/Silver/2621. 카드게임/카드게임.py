from collections import Counter

card_number = []
card_color = set()
for _ in  range(5):
	color, number = input().split()
	card_color.add(color)
	card_number.append(int(number))

card_number = sorted(card_number)
consecutive = True
for i in range(1, 5):
	if not(card_number[i-1] == card_number[i] - 1):
		consecutive = False
count_number = list(dict(Counter(card_number)).items())
count_number = sorted(count_number, key=lambda x:(-x[1],-x[0]))

score = 0
if len(card_color) == 1 and consecutive == True:
	score = card_number[-1] + 900
elif count_number[0][1] == 4:
	score = count_number[0][0] + 800
elif count_number[0][1] == 3 and count_number[1][1] == 2:
	score = count_number[0][0] * 10 + count_number[1][0] + 700
elif len(card_color) == 1:
	score = card_number[-1] + 600
elif consecutive == True:
	score = card_number[-1] + 500
elif count_number[0][1] == 3:
	score = count_number[0][0] + 400
elif count_number[0][1] == 2 and count_number[1][1] == 2:
	score = count_number[0][0] * 10 + count_number[1][0] + 300
elif count_number[0][1] == 2:
	score = count_number[0][0] + 200
else:
	score = card_number[-1] + 100

print(score)