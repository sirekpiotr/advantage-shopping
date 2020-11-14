import sys
import unittest
import HtmlTestRunner

sys.path.append('../')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.pages import *
from Resources.utilities import Utilities


class Test_User_Login_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_User_Login(Test_User_Login_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_show__login_modal(self):
        self.homePage = HomePage(self.driver)
        self.homePage.show_login_modal()

        self.assertIn(Utilities.HOME_POPUP_FACEBOOK_BUTTON_TEXT, self.homePage.driver.page_source)
        self.assertIn(Utilities.HOME_POPUP_USERNAME_TEXT, self.homePage.driver.page_source)
        self.assertIn(Utilities.HOME_POPUP_PASSWORD_TEXT, self.homePage.driver.page_source)

    def test_successfully_create_user_account(self):
        self.homePage = HomePage(self.driver)
        self.homePage.login_user()

        self.assertIn(Utilities.USERNAME, self.homePage.driver.page_source)

    def tearDown(self):
        super().tearDown()