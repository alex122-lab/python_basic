import time
import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """декоратор, который перед выполнением декорируемой функции ждёт несколько секунд."""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(*args, **kwargs)
        func(*args, **kwargs)
    return wrapped_func

@how_are_you
def test(time_sec):
    """функция для тестирования декоратора, который перед выполнением декорируемой функции ждёт несколько секунд."""
    print('Функция начала свою работу через', time_sec, 'с.')

test(3)