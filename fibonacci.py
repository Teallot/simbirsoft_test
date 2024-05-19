import datetime


class Fibonacci:
    @staticmethod
    def fib_current_day():
        # Получение текущей даты
        current_day = int(datetime.date.today().strftime('%d'))

        fib1 = fib2 = 1
        # Получение числа Фибоначчи для даты+1
        for i in range(2, current_day + 1):
            fib1, fib2 = fib2, fib1 + fib2

        return fib2
