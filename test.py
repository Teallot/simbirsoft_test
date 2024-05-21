import pytest
import allure
from simbirsoft_test.pom import Pages
from simbirsoft_test.conftest import setup_Chrome
from simbirsoft_test.fibonacci import Fibonacci
from simbirsoft_test.to_csv import ToCsv
from simbirsoft_test.results_allure import check


@pytest.mark.usefixtures('setup_Chrome')
class TestTransactions:
    def test_transactions(self):
        # Авторизация
        with allure.step('Authorisation'):
            pages = Pages(self.driver)
            pages.login_customer_click()
            pages.login_input()
            pages.login_select()
            pages.login_click()

        # Часть с пополнением счёта
        with allure.step('Deposit'):
            pages.deposit_click()
            current_day = Fibonacci.current_day()
            fib_current_day = Fibonacci.fib_current_day(current_day)
            pages.sum_input(fib_current_day)
            pages.deposit_add()

        # Часть со снятием со счёта
        with allure.step('Withdraw'):
            pages.withdraw_click()
            pages.sum_input(fib_current_day)
            pages.withdraw()

            assert pages.balance() == '0'

        # Переход на страницу транзакций и формирование словаря
        with allure.step('Transactions'):
            transaction_types = ['Credit', 'Debit']
            pages.transactions_click()
            transactions = pages.transactions_dict()

            # Формирование csv файла
            ToCsv.to_csv(transactions, 'transactions')

            assert transactions.get('Тип транзакции') == transaction_types
