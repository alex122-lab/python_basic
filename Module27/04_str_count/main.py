from typing import Callable, Any
import functools


def counter(func: Callable) -> Callable:
    """декоратор, считающий и выводящий количество вызовов декорируемой функции."""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        wrapped_func.count += 1
        res = func(*args, **kwargs)
        print('Функция {func} была вызвана: {count} раз'.format(
            func=func.__name__, count=wrapped_func.count))
        return res
    wrapped_func.count = 0
    return wrapped_func

@counter
def hello() -> None:
    """Функция, печатающая приветствие Hello World!"""
    print('Hello World!')

hello()
hello()
hello()
hello()