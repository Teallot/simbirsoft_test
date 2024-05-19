import time

import pytest
import allure_pytest
from simbirsoft_test.pom import Pages
from simbirsoft_test.conftest import setup
from simbirsoft_test.fibonacci import Fibonacci
import pandas as pd
from simbirsoft_test.results_allure import check


@pytest.mark.usefixtures(f'{setup}')
# Авторизация
class Authorization:
    def authorization(self):
        pages = Pages(self.driver)
        pages.login_customer_click()
        pages.login_input()
        pages.login_click()


@check
@pytest.mark.usefixtures(f'{setup}')
class TestTransactions:
    def test_transactions(self):
        # Часть с пополнением счёта
        pages = Pages(self.driver)
        Authorization.authorization(self)
        pages.deposit_click()
        fib_current_day = Fibonacci.fib_current_day()
        pages.sum_input(fib_current_day)
        pages.deposit_add()

        # Часть со снятием со счёта
        pages.withdrawl_click()
        time.sleep(2)
        fib_current_day = Fibonacci.fib_current_day()
        pages.sum_input(fib_current_day)
        pages.withdrawl()

        assert pages.balance() == '0'
        time.sleep(2)

        # Переход на страницу транзакций и формирование словаря
        transaction_types = ['Credit', 'Debit']
        pages.transactions_click()
        transactions = pages.transactions_dict()
        # Формирование csv файла
        df = pd.DataFrame(transactions)
        df.to_csv('transactions.csv', index=False, encoding='utf-8')

        assert transactions.get('Тип транзакции') == transaction_types
