# OOP

## 1. 개요

- OOP는 객체 지향 프로그래밍(*Object-Oriented Programming*)이다.

## 2. 기본 문법

- 클래스는 틀, 인스턴스는 사례이다. 클래스 = 사람, 인스턴스 = 아이유.
- 속성은 값, 메소드는 함수이다.

```python
# 클래스 정의 
class MyClass:
		pass
# 인스턴스 생성 
my_instance = MyClass() 
# 메서드 호출 
my_instance.my_method() 
# 속성 
my_instance.my_attribute
```
## 3. 인스턴스

- 인스턴스 변수: 인스턴스가 개인적으로 가지고 있는 속성이다. `self.<name>`으로 정의한다. 생성된 이후에는 `<instance>.<name>`으로 접근한다.

```python
class Person:
  
  def __init__(self, name):
    	self.name = name
      # 인스턴스 변수 정의
 
john = Person('john')
# 인스턴스 생성

print(john.name)
# john
# 인스턴스 변수 접근

john.name = 'John Kim'
# 인스턴스 변수 할당
print(john.name)
# John Kim
```
- 인스턴스 메소드: 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드이다. 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 전달된다.

```python
class MyClass:

  	def instance_method(self, arg1, ...):
```
- 생성자 메소드: 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드이다.

```python
class Person:

  	def __init__(self):
      print('인스턴스가 생성되었습니다.')

person1 = Person()
# 인스턴스가 생성되었습니다.

class Person:

  	def __init__(self, name):
      print(f'인스턴스가 생성되었습니다. {name}')

person1 = Person('지민')
# 인스턴스가 생성되었습니다. 지민
```
- 소멸자 메소드: 인스턴스 객체가 소멸되기 직전에 호출되는 메소드이다.

```python
class Person:

  	def __del__(self):
      print('인스턴스가 사라졌습니다.')

person1 = Person()
# 인스턴스가 사라졌습니다.
```
## 4. 클래스

- 클래스 속성: 한 클래스 안의 모든 인스턴스가 똑같은 값을 가진 속성이다. `<classname>.<name>`으로 접근 및 할당한다.

```python
class Circle:
  	pi = 3.14

c1 = Circle()
c2 = Circle()

print(Circle.pi)
# 3.14
print(C1.pi)
# 3.14
print(C2.pi)
# 3.14
```
- 클래스 메소드: 클래스가 사용하는 메소드이다. 호출 시, 첫 번째 인자로 클래스(cls)가 전달된다.

```python
 class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...):
 
MyClass.class_method(...)
```
- 스태틱 메소드: 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드이다. 속성을 다루지 않고 단지 기능만을 하는 메소드를 정의할 때 사용한다.

```python
 class MyClass:
    
    @staticmethod
    def class_method(arg1, ...):
      
MyClass.static_method(...)
```

- 클래스 메소드 정리

```python
 class MyClass:
    
    def method(self):
    	  return 'instace method', self
    
    @classmethod
    def class_method(cls):
     	  return 'class method', cls
      
    @staticmethod
    def static_method():  
     	  return 'static method'
```

## 5. 객체 지향의 핵심 개념

- 추상화
- 상속
- 다형성
- 캡슐화
