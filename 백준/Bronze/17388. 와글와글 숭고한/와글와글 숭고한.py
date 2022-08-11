s, k, h = map(int, input().split())
if s+k+h >= 100:
    print('OK')
else:
    rst = min([s, k, h])
    if rst == s:
        print('Soongsil')
    elif rst == k:
        print('Korea')
    else:
        print('Hanyang')