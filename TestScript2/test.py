import pytest
from base import BaseCase
from data import keys
from ui.locators.basic_locators import SegmentsPageLocators
import allure

class TestTarget(BaseCase):

    @allure.feature('UI tests')
    @allure.description("Checking a trying to log in with an invalid email")
    @pytest.mark.UI
    def test_invalid_login(self, login_page, bad_login_page):
        login_page.attempt_to_login(keys.BAD_MAIL, keys.PASSWORD)

        with allure.step("Checking for a page change with a message about incorrect entry"):
            assert bad_login_page.find(bad_login_page.locators.INVALID_LOGIN_LOCATOR).is_displayed()
            self.logger.info(f"Login attempt failed. Found: {bad_login_page.locators.INVALID_LOGIN_LOCATOR}")

    @allure.feature('UI tests')
    @allure.description("Checking a trying to log in with an invalid password")
    @pytest.mark.UI
    def test_invalid_pass(self, login_page, bad_login_page):
        login_page.attempt_to_login(keys.MAIL, keys.BAD_PASSWORD)
        with allure.step("Checking for a page change with a message about incorrect entry"):
            assert bad_login_page.find(bad_login_page.locators.INVALID_LOGIN_LOCATOR).is_displayed()
            self.logger.info(f"Login attempt failed. Found: {bad_login_page.locators.INVALID_LOGIN_LOCATOR}")

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a campaign")
    @pytest.mark.UI
    def test_create_campaign(self,file_path, dashboard_page):
        campaign_name = dashboard_page.create_campaign(file_path)
        with allure.step("Checking if a campaign has been created"):
            assert dashboard_page.campaign_exist(campaign_name)
            self.logger.info(f"Campaign named {campaign_name} successfully created")

    @allure.feature('UI tests')
    @allure.description("Checking the creation of a segment")
    @pytest.mark.skip
    def test_create_segment(self, segments_page):
        segment_name = segments_page.create_segment()
        with allure.step("Checking that the segment has been created"):
            all_segments = [name.text for name in segments_page.find_all(SegmentsPageLocators.ALL_SEGMENTS)]
            assert segment_name in all_segments
            self.logger.info(f"Segment named {segment_name} successfully created")
            segments_page.delete_segment(segment_name)

    @allure.feature('UI tests')
    @allure.description("Checking the deletion created segment")
    @pytest.mark.skip
    def test_delete_segment(self, segments_page):
        bool_assert = False
        segment_name = segments_page.create_segment()
        segments_page.delete_segment(segment_name)
        segments_page.driver.refresh()
        with allure.step("Checking that the segment has been deleted"):
            all_segments = [name.text for name in segments_page.find_all(SegmentsPageLocators.ALL_SEGMENTS)]
            assert segment_name not in all_segments
            self.logger.info(f"Segment named {segment_name} successfully deleted")