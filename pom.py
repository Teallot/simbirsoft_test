from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from simbirsoft_test.locators import locators


class Pages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)


    # Переход к странице авторизации
    def login_customer_click(self):
        btn_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, locators.get('btn_login'))))
        btn_login.click()
        return btn_login

    # Выбор клиента Harry Potter
    def login_input(self):
        input_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, locators.get('login_input'))))
        input_login.click()
        return input_login

    def login_select(self):
        select_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, locators.get('login_hp'))))
        select_login.click()
        return select_login

    # Авторизация
    def login_click(self):
        login = self.wait.until(ec.element_to_be_clickable((By.XPATH,  locators.get('login_click'))))
        login.click()
        return login

    # Получение баланса
    def balance(self):
        balance_elem = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locators.get('balance'))))
        balance = balance_elem.get_attribute('textContent')
        return balance

    # Переход к пополнению
    def deposit_click(self):
        deposit = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locators.get('deposit_move'))))
        deposit.click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[text()="Amount to be Deposited :"]')))
        return deposit

    # Ввод суммы
    def sum_input(self, fib):
        sum_input = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locators.get('sum_input'))))
        sum_input.send_keys(fib)
        return sum_input

    # Пополнение
    def deposit_add(self):
        add = self.wait.until(ec.element_to_be_clickable((By.XPATH, locators.get('deposit_transaction'))))
        add.click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[text()="Deposit Successful"]')))
        return add

    # Переход к снятию
    def withdraw_click(self):
        withdraw_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locators.get('withdraw_move'))))
        withdraw_btn.click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[text()="Amount to be Withdrawn :"]')))
        return withdraw_btn

    # Снятие
    def withdraw(self):
        withdraw = self.wait.until(ec.element_to_be_clickable((By.XPATH,  locators.get('withdraw_transaction'))))
        withdraw.click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[text()="Transaction successful"]')))
        return withdraw

    # Переход к истории операций
    def transactions_click(self):
        transactions_btn = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, locators.get('transactions_move'))))
        transactions_btn.click()
        return transactions_btn

    # Получение словаря транзакций
    def transactions_dict(self):

        self.driver.implicitly_wait(10)
        transactions = []
        for i in range(2):
            transactions.append([])
            for j in range(3):
                transactions[i].append(self.driver.find_element(By.XPATH, f'// *[ @ id = "anchor{i}"] / td[{j + 1}]').text)
        # Получение необходимого формата даты
        date_trans = [transactions[0][0].split(' '), transactions[1][0].split(' ')]
        for i in range(len(date_trans)):
            date_trans[i][0], date_trans[i][1] = date_trans[i][1],  date_trans[i][0]
        # Получение словаря
        transactions = {
            'Дата-время транзакции': [' '.join(date_trans[0]), ' '.join(date_trans[1])],
            'Сумма': [int(transactions[0][1]), int(transactions[1][1])],
            'Тип транзакции': [transactions[0][2], transactions[1][2]]
        }

        return transactions

