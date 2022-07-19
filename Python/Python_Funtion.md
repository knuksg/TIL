# Python_Fuction

## Sort(key= , reverse=True/False)

```python
x = [{'a' : 10, 'b' : 20, 'c' : 30}, {'a' : 20, 'b' : 2, 'c' : 1}, {'a' : 20, 'b' : 30, 'c' : 10}]
# x는 딕셔너리를 요소로 가진 리스트!
print(x[0]['a'])
# x의 0번째 딕셔너리 의 'a' 값인 10이 출력된다.

#sort(key=lamda)를 사용할 때는 '요소'값만 있으면 된다.
x.sort(key=lambda x : x['a'])
# [{'a': 10, 'b': 20, 'c': 30}, {'a': 20, 'b': 2, 'c': 1}, {'a': 20, 'b': 30, 'c': 10}]
# 'a' 값을 기준으로 정렬된 모습.

x = [{'a' : 10, 'b' : 20, 'c' : 30}, {'a' : 20, 'b' : 2, 'c' : 1}, {'a' : 20, 'b' : 30, 'c' : 10}]
x.sort(key=lambda x : (x['a'], x['c']))
# [{'a': 10, 'b': 20, 'c': 30}, {'a': 20, 'b': 2, 'c': 1}, {'a': 20, 'b': 30, 'c': 10}]
# 'a' 값을 기준으로 정렬하고, 'a' 값이 같으면 그 다음 'c' 값으로 정렬.




```
