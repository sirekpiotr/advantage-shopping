from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from Resources.locators import Locators
from Resources.utilities import Utilities


class BasePage:

    """This class is the parent class for all the pages in shopping application."""

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        time.sleep(Utilities.DEFAULT_WAIT)

    def wait_until_visible(self, by_locator):
        WebDriverWait(self.driver, Utilities.DEFAULT_WAIT)\
            .until(EC.visibility_of_element_located(by_locator))

    def wait_unit_not_visible(self, by_locator):
        WebDriverWait(self.driver, Utilities.DEFAULT_WAIT)\
            .until(EC.invisibility_of_element_located(by_locator))

    def wait_until_clickable(self, by_locator):
        WebDriverWait(self.driver, Utilities.DEFAULT_WAIT)\
            .until(EC.element_to_be_clickable(by_locator))

    def click(self, by_locator):
        WebDriverWait(self.driver, Utilities.DEFAULT_WAIT)\
            .until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, text):
        element = WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator))
        assert element.text == text

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator)).text

    def check_number_of_elements(self, by_locator):
        elements = WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_all_elements_located(by_locator))

        return len(elements)

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text(self, by_locator):
        WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator)).clear()

    def is_visible(self, by_locator):
        return WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator)).is_visible()

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, Utilities.DEFAULT_WAIT) \
            .until(EC.visibility_of_element_located(by_locator)).is_enabled()

    def get_text_from_element(self, by_locator):
        return WebDriverWait(self.driver, Utilities.DEFAULT_WAIT)\
            .until(EC.visibility_of_element_located(by_locator)).text


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Utilities.BASE_URL)

    def search_our_products_container(self):
        self.driver.find_element(Locators.HOME_PAGE_OUR_PRODUCTS_CONTAINER)

    def search_products(self):
        self.click(Locators.HOME_SEARCH_BUTTON)

        self.clear_text(Locators.HOME_SEARCH_FIELD)
        self.enter_text(Locators.HOME_SEARCH_FIELD, Utilities.BASE_SEARCH_TERM)
        self.enter_text(Locators.HOME_SEARCH_FIELD, Keys.ENTER)

        self.wait_until_visible(Locators.SEARCH_RESULTS_HEADLINE)

    def search_null_products(self):
        self.click(Locators.HOME_SEARCH_BUTTON)

        self.clear_text(Locators.HOME_SEARCH_FIELD)
        self.enter_text(Locators.HOME_SEARCH_FIELD, Utilities.BASE_SEARCH_NEGATIVE_TERM)
        self.enter_text(Locators.HOME_SEARCH_FIELD, Keys.ENTER)

        self.wait_until_visible(Locators.SEARCH_FAILED_HEADLINE)

    def go_to_headphone_category(self):
        self.click(Locators.HOME_HEADPHONE_CATEGORY_BUTTON)
        self.wait_until_visible(Locators.CATEGORY_HEADER)

    def go_to_speaker_category(self):
        self.click(Locators.HOME_SPEAKER_CATEGORY_BUTTON)
        self.wait_until_visible(Locators.CATEGORY_HEADER)

    def go_to_laptop_category(self):
        self.click(Locators.HOME_LAPTOPS_CATEGORY_BUTTON)
        self.wait_until_visible(Locators.CATEGORY_HEADER)

    def go_to_tablet_category(self):
        self.click(Locators.HOME_TABLETS_CATEGORY_BUTTON)
        self.wait_until_visible(Locators.CATEGORY_HEADER)

    def go_to_mice_category(self):
        self.click(Locators.HOME_MICE_CATEGORY_BUTTON)
        self.wait_until_visible(Locators.CATEGORY_HEADER)

    def show_login_modal(self):
        self.click(Locators.HOME_USER_LOGIN_BUTTON)
        self.wait_until_visible(Locators.HOME_POPUP)

    def login_user(self):
        self.click(Locators.HOME_USER_LOGIN_BUTTON)
        self.wait_until_visible(Locators.HOME_POPUP)

        self.click(Locators.HOME_POPUP_USERNAME_FIELD)
        self.clear_text(Locators.HOME_POPUP_USERNAME_FIELD)
        self.enter_text(Locators.HOME_POPUP_USERNAME_FIELD, Utilities.USERNAME)

        self.wait()

        self.click(Locators.HOME_POPUP_PASSWORD_FIELD)
        self.clear_text(Locators.HOME_POPUP_PASSWORD_FIELD)
        self.enter_text(Locators.HOME_POPUP_PASSWORD_FIELD, Utilities.PASSWORD)

        self.click(Locators.HOME_POPUP_SUBMIT_BUTTON)
        self.wait_unit_not_visible(Locators.HOME_POPUP)


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_number_of_searched_products(self):
        return self.check_number_of_elements(Locators.PRODUCT_IMAGE)


class CategoryResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_number_of_elements_in_category(self):
        return self.check_number_of_elements(Locators.PRODUCT_NAME_HEADLINE)

    def get_text_of_header_headline(self):
        return self.get_text_from_element(Locators.CATEGORY_HEADER_HEADLINE)

    def get_text_of_header_sub_headline(self):
        return self.get_text_from_element(Locators.CATEGORY_HEADER_SUB_HEADLINE)

    def get_text_of_header_note(self):
        return self.get_text_from_element(Locators.CATEGORY_HEADER_NOTE)


