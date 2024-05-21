import datetime


class Fibonacci:
    @staticmethod
    def current_day():
        # Получение текущей даты
        current_day = int(datetime.date.today().strftime('%d'))

        return current_day

    @staticmethod
    def fib_current_day(day):
        fib1 = fib2 = 1
        # Получение числа Фибоначчи для даты+1
        for i in range(day + 1):
            fib1, fib2 = fib2, fib1 + fib2

        return fib2
