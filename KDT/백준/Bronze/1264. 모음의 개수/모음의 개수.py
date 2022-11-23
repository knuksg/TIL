while True:
    w = input()
    if w == '#':
        break
    rst = 0
    rst += w.count('a')
    rst += w.count('e')
    rst += w.count('i')
    rst += w.count('o')
    rst += w.count('u')
    rst += w.count('A')
    rst += w.count('E')
    rst += w.count('I')
    rst += w.count('O')
    rst += w.count('U')
    print(rst)