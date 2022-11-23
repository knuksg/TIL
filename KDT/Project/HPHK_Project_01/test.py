x = [{'a' : 10, 'b' : 20, 'c' : 30}, {'a' : 20, 'b' : 2, 'c' : 1}, {'a' : 20, 'b' : 30, 'c' : 10}]
x.sort(key=lambda x : (x['a'], x['c']))
print(x)

