with open('3회차/김선교/data/fruits.txt', 'r', encoding='utf-8') as f:
    berrys = f.read()
    real_berry = berrys.split('\n')
    rst = set()
    for i in real_berry:
        if i.endswith('berry'):
            rst.add(i+'\n')
    print(len(rst))
    for i in rst:
        print(i)
with open('02.txt', 'w', encoding='utf-8') as f2:
    f2.write(str(len(rst))+'\n')
    f2.writelines(rst)