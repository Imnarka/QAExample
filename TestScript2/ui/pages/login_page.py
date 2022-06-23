from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from ui.locators.basic_locators import InvalidLoginLocators
import allure

class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Authorization")
    def attempt_to_login(self, email, password):
        self.wait_locator(LoginPageLocators.SPINNER_LOCATOR)
        self.logger.info(f"Authorization attempt with login:{email} and password: {password}")
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.send_data(LoginPageLocators.EMAIL_LOCATOR, email)
        self.send_data(LoginPageLocators.PASSWORD_LOCATOR, password)
        self.click(LoginPageLocators.AUTH_LOCATOR)