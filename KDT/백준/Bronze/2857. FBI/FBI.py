FBI = False
for i in range(5):
    name = input()
    if 'FBI' in name:
        print(i+1, end=' ')
        FBI = True
if FBI == False:
    print('HE GOT AWAY!')