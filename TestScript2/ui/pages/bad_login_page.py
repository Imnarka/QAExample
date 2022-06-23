from ui.pages.base_page import BasePage
from ui.locators.basic_locators import InvalidLoginLocators
import allure

class InvalidLoginPage(BasePage):
    locators = InvalidLoginLocators()