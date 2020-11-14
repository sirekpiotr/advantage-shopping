import sys
import unittest
import HtmlTestRunner

sys.path.append('../')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.pages import *
from Resources.utilities import Utilities


class Test_Search_Products_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_Search_Products(Test_Search_Products_Base):

    def setUp(self):
        super().setUp()

    # Test with correct product name which is  in database. Website should return page with products.

    def test_successful_search(self):
        self.homePage = HomePage(self.driver)
        self.homePage.search_products()
        self.searchResultsPage = SearchResultsPage(self.driver)

        self.assertIn(Utilities.BASE_FOUND_TERM, self.searchResultsPage.driver.page_source)
        self.assertNotIn(Utilities.BASE_NOT_FOUND_TERM, self.searchResultsPage.driver.page_source)

    # Test for invalid product name which is not in database. Website should return "Not found" page.

    def test_negative_search(self):
        self.homePage = HomePage(self.driver)
        self.homePage.search_null_products()
        self.searchResultsPage = SearchResultsPage(self.driver)

        self.assertIn(Utilities.BASE_NOT_FOUND_TERM, self.searchResultsPage.driver.page_source)
        self.assertNotIn(Utilities.BASE_FOUND_TERM, self.searchResultsPage.driver.page_source)

    # Test that full number of products on one page loaded successfully

    def test_number_of_searched_products(self):
        self.homePage = HomePage(self.driver)
        self.homePage.search_products()
        self.searchResultsPage = SearchResultsPage(self.driver)
        self.numberOfProducts = self.searchResultsPage.get_number_of_searched_products()

        self.assertEqual(self.numberOfProducts, 24)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner
                  .HTMLTestRunner(output='../Reports'))
