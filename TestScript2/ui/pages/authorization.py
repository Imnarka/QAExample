from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage
from ui.locators.basic_locators import AuthPageLocators
from ui.pages.segments_page import SegmentPage
import allure

class AuthPage(BasePage):
    locators = AuthPageLocators()

    @allure.step("Select Dashboard page")
    def go_to_dashboard(self):
        self.click(AuthPageLocators.DASHBOARD_LOCATOR)
        return DashboardPage(self.driver)

    @allure.step("select the Segment page")
    def go_to_segments(self):
        self.click(AuthPageLocators.SEGMENTS_LOCATOR)
        return SegmentPage(self.driver)