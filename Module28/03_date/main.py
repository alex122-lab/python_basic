class Date:
    """
    класс `Date`:
    - проверяет числа даты на корректность;
    - конвертирует строку даты в объект класса `Date`.
     """
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
       return f'День: {self.day}\tМесяц: {self.month}\tГод:{self.year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """метод проверяет числа даты на корректность"""
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Data':
        """метод конвертирует строку даты в объект класса `Date`."""
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj



date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# 2 вариант метода проверки числа даты на корректность
# from datetime import datetime
# @classmethod
# def is_date_valid(cls, data: str) -> bool:
#     """метод проверяет числа даты на корректность"""
#     format = "%d-%m-%Y"
#     try:
#         res = bool(datetime.strptime(data, format))
#     except ValueError:
#         res = False
#     return res

