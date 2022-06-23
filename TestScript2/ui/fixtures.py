import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.bad_login_page import InvalidLoginPage
from ui.pages.authorization import AuthPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segments_page import SegmentPage
from data import keys
import os
from _pytest.fixtures import FixtureRequest
import allure


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def bad_login_page(driver):
    return InvalidLoginPage(driver=driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def dashboard_page(login):
    return login.go_to_dashboard()

@pytest.fixture
def segments_page(login):
    return login.go_to_segments()

def get_driver():
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())

    browser.maximize_window()
    browser.get("https://target.my.com/")

    return browser

@pytest.fixture(scope='function')
def driver():

    with allure.step("Initialization driver"):
        browser = get_driver()
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def cookies():
    driver = get_driver()
    driver.get("https://target.my.com/")
    login_page = LoginPage(driver)
    login_page.attempt_to_login(keys.MAIL, keys.PASSWORD)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, "data", "cf466bc38f9173cc034b2656e9e09fab.png")

@pytest.fixture(scope='function')
def login(driver, request: FixtureRequest, auth_page):
    with allure.step("Get cookies"):
        cookies = request.getfixturevalue('cookies')
    with allure.step("Add cookies"):
        for cookie in cookies:
            driver.add_cookie(cookie)
    with allure.step("Refresh page"):
        driver.refresh()

    yield auth_page