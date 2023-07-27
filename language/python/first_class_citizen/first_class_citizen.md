# **일급 객체(First-class citizen)란?**

일급객체는 다음의 조건을 만족한다.

**1. 변수 혹은 데이터 구조(자료구조) 안에 담을 수 있어야 한다.**

**2. 매개변수로 전달할 수 있어야 한다.**

**3. 리턴값으로 사용될 수 있어야 한다.**

# python의 일급객체

- 함수를 선언하게 되면 함수를 관리하기 위한 PyFunctionObject를 생성하게 된다. 즉, 함수의 이름은 함수 객체를 가리키는 참조 변수이다.
- python에서 함수는 객체이며 함수도 일급객체로 사용된다. 그래서 다음과 같은 조건을 만족한다.

```python
# 1.변수 혹은 데이터구조 안에 함수를 담을 수 있다.
def plus(a: int, b: int) -> int:
    return a + b


fun1 = plus

print(fun1)
print(plus)
print(fun1 is plus)

test_list = list[plus(1, 2), 1]
print(test_list)


#결과
<function plus at 0x10262c160>
<function plus at 0x10262c160>
True
list[3, 1]



# 2.매개변수로 함수를 전달할 수 있다.
def add(a, b):
    return a + b


def print_add(func, x, y):
    print(func(x, y))


print_add(add, 1, 2)  # 매개변수로 add함수를 전달하고 3을 출력하게 됨

#결과
3


# 3.함수를 리턴값으로 사용할 수 있다.
def hello(name):
    def formatting():
        print(f"Hello, My name is {name}")
    return formatting()


hello("Jiye")

#결과
Hello, My name is Jiye
```