import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium import webdriver


@pytest.fixture
def get_webdriver_Chrome(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"

    return driver


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.headless = False # Если нужно включить UI кидаем false
    options.add_argument('chrome')
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture(scope='function')
def setup_Chrome(request, get_webdriver_Chrome):
    driver = get_webdriver_Chrome
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
