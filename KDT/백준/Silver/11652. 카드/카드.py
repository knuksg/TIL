n = int(input())
numbers = {}
for i in range(n):
    number = input()
    numbers[number] = numbers.get(number, 0) + 1
max_ = 0
for i in numbers:
    if numbers[i] > max_:
        max_ = numbers[i]
max_list = []        
for i in numbers:
    if numbers[i] == max_:
        max_list.append(int(i))
print(sorted(max_list)[0])