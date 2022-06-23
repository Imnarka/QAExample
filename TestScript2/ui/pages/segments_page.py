from uuid import uuid4
from ui.pages.login_page import LoginPage
from ui.locators.basic_locators import SegmentsPageLocators
import allure

class SegmentPage(LoginPage):

    locators = SegmentsPageLocators()

    @allure.step("Trying to create a segment")
    def create_segment(self):
        SOME_VALUE = 1234

        self.wait_locator(SegmentsPageLocators.SPINNER_LOCATOR)
        try:
            self.click(SegmentsPageLocators.CREATE_SEGMENT_LOCATOR, 5)
        except:
            self.click(SegmentsPageLocators.NEW_SEGMENT_LOCATOR, 5)

        self.click(SegmentsPageLocators.SELECT_SEGMENT_LOCATOR)
        self.click(SegmentsPageLocators.SEGMENT_SOURCE_CHECKBOX_LOCATOR)
        self.click(SegmentsPageLocators.SUBMIT_ADD_LOCATOR)
        self.send_data(SegmentsPageLocators.SEGMENT_NAME_LOCATOR, SOME_VALUE, False)
        segment_name = self.find(SegmentsPageLocators.SEGMENT_NAME_LOCATOR).get_attribute("value")

        self.click(SegmentsPageLocators.SUBMIT_CREATE_SEGMENT_LOCATOR)

        return segment_name

    @allure.step("Trying to delete a segment")
    def delete_segment(self, segment_name):
        self.click((SegmentsPageLocators.DELETE_SEGMENT_LOCATOR[0], SegmentsPageLocators.DELETE_SEGMENT_LOCATOR[1].
                    format(segment_name)))
        self.click(SegmentsPageLocators.SUBMIT_DELETE_LOCATOR)