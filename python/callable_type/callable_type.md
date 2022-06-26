python의 경우 함수도 일급객체이기 때문에 함수를 인자로 리턴할 수 있다.

이런 함수의 typing 작성방법이 Callable types를 가리킨다.

`Callble[[인자의 타입, …], return될 타입]`

- 첫 번째 인자: 인자 값들에 대한 타입
- 두 번재 인자: return될 타입

```python
from typing import Callable

def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)

def add(a: int, b: int) -> int:
    return a + b

print(foo(add)) # 결과: 5
```