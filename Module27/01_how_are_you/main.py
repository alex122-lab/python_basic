from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """декоратор how_are_you, который делает ненужные комментарии"""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Как дела? Хорошо.')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrapped_func

@how_are_you
def test():
    """функция для тестирования декоратора"""
    print('<Тут что-то происходит...>')

@how_are_you
def test_2():
    """функция для тестирования декоратора"""
    print('<Непонятно что произошло...>')

test()
print()
test_2()