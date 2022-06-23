from selenium.webdriver.common.by import By

class BasePageLocators:
    SPINNER_LOCATOR = (By.CSS_SELECTOR, "div[class^='spinner']")

class AuthPageLocators(BasePageLocators):
    DASHBOARD_LOCATOR = (By.XPATH, "//a[contains(text(),'Кампании')]")
    SEGMENTS_LOCATOR = (By.XPATH, "//a[contains(text(),'Аудитории')]")

class DashboardPageLocators(AuthPageLocators):
    NEW_CAMPAIGN_LOCATOR = (By.CSS_SELECTOR, "a[href='/campaign/new']")
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'dashboard-module-createButtonWrap')]/div")
    TRAFFIC_LOCATOR = (By.XPATH, "//div[contains(@class, 'traffic')]")
    LINK_LOCATOR = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput')]")
    CAMPAIGN_NAME_LOCATOR = (By.XPATH, "//div[@class='input__wrap']/input")
    FORMAT_LOCATOR = (By.XPATH, "//div[@id='patterns_banner_4']")
    UPLOAD_LOCATOR = (By.XPATH, "//input[contains(@data-test, 'image_240x400')]")
    SUBMIT_IMAGE = (By.XPATH, "//input[contains(@class, 'js-save')]")
    UPLOAD_PROCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'roles-module-uploadButton')]")
    SUBMIT_CREATE_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]/button")

class InvalidLoginLocators(BasePageLocators):
    INVALID_LOGIN_LOCATOR = (By.XPATH, "//div[contains(text(),'Invalid login or password')]")

class LoginPageLocators(BasePageLocators):
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    AUTH_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

class SegmentsPageLocators(AuthPageLocators):
    NEW_SEGMENT_LOCATOR = (By.CSS_SELECTOR, "a[href='/segments/segments_list/new/']")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-create-button-wrap')]/button")
    SUBMIT_ADD_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-add-button')]/button")
    SELECT_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and text()='Приложения и игры в соцсетях']")
    SEGMENT_SOURCE_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "input[class^='adding-segments-source__checkbox']")
    SUBMIT_CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-create-segment-button-wrap')]/button")
    SEGMENT_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]/div[@class='input__wrap']/input")
    SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']")
    DELETE_SEGMENT_LOCATOR = (By.XPATH, "//a[@title='{}']/ancestor::div/following-sibling::div[4]/span")
    SUBMIT_DELETE_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
    ALL_SEGMENTS = (By.XPATH, "//div[contains(@class, 'main-module-Table')]//a[contains(@href, '/segments/segments_list')]")
