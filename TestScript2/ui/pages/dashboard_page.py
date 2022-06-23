from ui.pages.base_page import BasePage
from ui.locators.basic_locators import DashboardPageLocators
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
import time
from selenium.webdriver.common.by import By
import allure

def wait(method, error=Exception, timeout=20, interval=0.5, **kwargs):
    started = time.time()
    while time.time() - started < timeout:
        try:
            method(**kwargs)
            return
        except error:
            pass
    raise TimeoutException(f'Method {method.__name__} timeout out')


class DashboardPage(BasePage):
    locators = DashboardPageLocators()

    @allure.step("Trying to create a company")
    def create_campaign(self, file_path):

        SOME_VALUE = 9641

        self.wait_locator(DashboardPageLocators.SPINNER_LOCATOR)
        try:
            self.click(DashboardPageLocators.CREATE_CAMPAIGN_LOCATOR)
        except:
            self.click(DashboardPageLocators.NEW_CAMPAIGN_LOCATOR)
        self.wait_locator(DashboardPageLocators.SPINNER_LOCATOR)
        self.click(DashboardPageLocators.TRAFFIC_LOCATOR)
        self.send_data(DashboardPageLocators.LINK_LOCATOR, 'https://vk.com/lmnarka')
        wait(self.send_data, error=ElementNotInteractableException, locator=DashboardPageLocators.CAMPAIGN_NAME_LOCATOR,
             data = SOME_VALUE, clear = False)
        campaign_name = self.find(DashboardPageLocators.CAMPAIGN_NAME_LOCATOR).get_attribute("value")
        self.click(DashboardPageLocators.FORMAT_LOCATOR)
        input_field = self.find(DashboardPageLocators.UPLOAD_LOCATOR)
        input_field.send_keys(file_path)
        self.click(DashboardPageLocators.SUBMIT_IMAGE)
        self.wait_locator(DashboardPageLocators.UPLOAD_PROCESS_LOCATOR)
        self.click(DashboardPageLocators.SUBMIT_CREATE_LOCATOR)
        return campaign_name

    def campaign_exist(self, campaign_name):
        locator = (By.XPATH, f"//a[contains(@title,'{str(campaign_name)}')]")
        return len(self.find_all(locator, timeout=15)) != 0