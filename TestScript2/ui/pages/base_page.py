import logging
from ui.locators.basic_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

CLICK_RETRY = 3


class BasePage(object):

    locators = BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')

    def wait(self, timeout=None):

        if timeout is None:
            timeout = 30
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step("Trying to find {locator}")
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Trying to find {locator}")
    def find_all(self, locator, timeout=None):
        self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Waiting for the load")
    def wait_locator(self, locator):
        try:
            self.wait(10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return
        self.wait(20).until(EC.invisibility_of_element_located(locator))

    @allure.step("Click on {locator}")
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException):
                if i == CLICK_RETRY-1:
                    raise

    @allure.step("Send data to {locator}")
    def send_data(self, locator, data, clear=True):
        elem = self.find(locator)
        if clear:
            elem.clear()
        elem.send_keys(data)