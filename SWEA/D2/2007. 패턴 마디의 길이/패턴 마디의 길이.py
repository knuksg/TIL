for i in range(int(input())):
    w = input()
    set_ = set(w.split(w[0])[1:-1])
    result = ''.join(set_)
    print(f'#{i+1} {len(result)+len(set_)}')