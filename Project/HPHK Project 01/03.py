with open('3회차/김선교/data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruit = text.split()

    berry_dic = {}
    for i in fruit:
        berry_dic[i] = berry_dic.get(i, 0) + 1
        
with open('03.txt', 'w', encoding='utf-8') as f2:
    x = list(berry_dic.keys())
    y = list(berry_dic.values())
    for i in y:
        y = map(str, y)

    for i, ii in zip(x,y):
        f2.write(i)
        f2.write(' ')
        f2.write(ii)
        f2.write('\n')