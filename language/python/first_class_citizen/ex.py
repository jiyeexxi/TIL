# 1.변수 혹은 데이터구조 안에 함수를 담을 수 있다.
def plus(a: int, b: int) -> int:
    return a + b


fun1 = plus

print(fun1)
print(plus)
print(fun1 is plus)

test_list = list[plus(1, 2), 1]
print(test_list)


# 2.매개변수로 함수를 전달할 수 있다.
def add(a, b):
    return a + b


def print_add(func, x, y):
    print(func(x, y))


print_add(add, 1, 2)  # 매개변수로 add함수를 전달하고 3을 출력하게 됨


# 3.함수를 리턴값으로 사용할 수 있다.
def hello(name):
    def formatting():
        print(f"Hello, My name is {name}")
    return formatting()


hello("Jiye")
