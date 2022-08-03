a, b = input().split()
list_a = list(a)
list_b = list(b)
a5 = ''
b5 = ''
a6 = ''
b6 = ''
for i in range(len(list_a)):
    if list_a[i] == '5':
        a5 += '5'
        a6 += '6'
    elif list_a[i] == '6':
        a5 += '5'
        a6 += '6'
    else:
        a5 += list_a[i]
        a6 += list_a[i]
for i in range(len(list_b)):
    if list_b[i] == '5':
        b5 += '5'
        b6 += '6'
    elif list_b[i] == '6':
        b5 += '5'
        b6 += '6'
    else:
        b5 += list_b[i]
        b6 += list_b[i]
print(int(a5)+int(b5), int(a6)+int(b6), sep=' ')