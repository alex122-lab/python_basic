from typing import Callable, Any
import functools
from functools import lru_cache


def cache_decorator(func: Callable) -> Callable:
    """декоратор, который кэширует (сохраняет для дальнейшего использования)
    результаты вызова функции и, при повторном вызове с теми же аргументами,
    возвращает сохранённый результат. """

    @functools.wraps(func)
    def wrapper_func(*args) -> int:
        if args in wrapper_func.cache:
            return wrapper_func.cache[args]
        else:
            result = func(*args)
            wrapper_func.cache[args] = result
            return result

    wrapper_func.cache = dict()
    return wrapper_func

@cache_decorator
def fibonacci(number) -> int:
    """рекурсивная функция, вычисляющая числа Фибоначчи"""
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован
# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша
# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован