from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор, который отвечает за логирование функций.
    Если во время выполнения декорируемой функции возникла ошибка,
    то в файл function_errors.log записываются название функции и ошибки.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'\nНазвание функции: {func.__name__}.'
              f'\nДокументация:{func.__doc__}')

        timeNow = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            with open('function_errors.log', 'a', encoding='utf-8') as f:
                f.write(f'{timeNow} Название функции: [{func.__name__}]. '
                        f'Исключение: [{type(e).__name__}]. Ошибка: [{e}]\n')

    return wrapped_func

@logging
def func_square() -> int:
    """ Функция возводит число в квадрат. """
    num1 = int(input('Введите число: '))
    resalt = num1
    return resalt


@logging
def func_div() -> float:
    """ Функция делит первое введенное пользователем число на второе. """
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    # number_int = int(input('Введите число: '))
    result = num1 / num2
    return result

func_square()
func_div()
