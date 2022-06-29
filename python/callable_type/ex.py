from typing import Callable


def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)


def add(a: int, b: int) -> int:
    return a + b


print(foo(add))
