from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Pages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # Переход к странице авторизации
    def login_customer_click(self):
        btn_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Customer Login"]')))
        btn_login.click()
        return btn_login

    # Выбор клиента Harry Potter
    def login_input(self):
        input_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="userSelect"]')))
        input_login.click()
        select_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="userSelect"]/option[text()="Harry Potter"]')))
        select_login.click()
        return select_login

    # Авторизация
    def login_click(self):
        login = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Login"]')))
        login.click()
        return login

    # Получение баланса
    def balance(self):
        balance_elem = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/strong[2]')))
        balance = balance_elem.get_attribute('textContent')
        return balance

    # Переход к пополнению
    def deposit_click(self):
        deposit = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]')))
        deposit.click()
        return deposit

    # Ввод суммы
    def sum_input(self, fib):
        sum_input = self.wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')))
        sum_input.send_keys(fib)
        return sum_input

    # Пополнение
    def deposit_add(self):
        add = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')))
        add.click()
        return add

    # Переход к снятию
    def withdrawl_click(self):
        withdrawl_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[3]')))
        withdrawl_btn.click()
        return withdrawl_btn

    # Снятие
    def withdrawl(self):
        withdrawl = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/button')))
        withdrawl.click()
        return withdrawl

    # Переход к истории операций
    def transactions_click(self):
        transactions_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]')))
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

