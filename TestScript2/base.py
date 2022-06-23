import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
import os
import allure

class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            screenshot = os.path.join(temp_dir, 'fail.png')
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, 'fail.png', attachment_type=allure.attachment_type.PNG)
            browser_log = os.path.join(temp_dir, 'browser.log')
            with open(browser_log, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

            with open(browser_log, 'r') as f:
                allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.logger = logger