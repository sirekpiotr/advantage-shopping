import sys
import unittest
import HtmlTestRunner

sys.path.append('../')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.pages import *
from Resources.utilities import Utilities


class Test_Products_Categories_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_Headphone_Products_Category(Test_Products_Categories_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_loaded_headphone_header(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_headphone_category()

        self.headphonesCategoryPage = CategoryResultsPage(self.driver)
        self.headphonesCategoryHeaderHeadline = self.headphonesCategoryPage.get_text_of_header_headline()
        self.headphonesCategoryHeaderSubHeadline = self.headphonesCategoryPage.get_text_of_header_sub_headline()
        self.headphonesCategoryHeaderNote = self.headphonesCategoryPage.get_text_of_header_note()

        self.assertEqual(self.headphonesCategoryHeaderHeadline, Utilities.HEADPHONE_HEADER_HEADLINE_TEXT)
        self.assertEqual(self.headphonesCategoryHeaderSubHeadline, Utilities.HEADPHONE_HEADER_SUB_HEADLINE_TEXT)
        self.assertEqual(self.headphonesCategoryHeaderNote, Utilities.HEADPHONE_HEADER_NOTE_TEXT)

    def test_successfully_loaded_all_headphones(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_headphone_category()

        self.headphonesCategoryPage = CategoryResultsPage(self.driver)
        self.headphonesNumber = self.headphonesCategoryPage.get_number_of_elements_in_category()

        self.assertEqual(self.headphonesNumber, 4)

    def tearDown(self):
        super().tearDown()


class Test_Speaker_Products_Category(Test_Products_Categories_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_loaded_speaker_header(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_speaker_category()

        self.speakersCategoryPage = CategoryResultsPage(self.driver)
        self.speakersCategoryHeaderHeadline = self.speakersCategoryPage.get_text_of_header_headline()
        self.speakersCategoryHeaderSubHeadline = self.speakersCategoryPage.get_text_of_header_sub_headline()
        self.speakersCategoryHeaderNote = self.speakersCategoryPage.get_text_of_header_note()

        self.assertEqual(self.speakersCategoryHeaderHeadline, Utilities.SPEAKER_HEADER_HEADLINE_TEXT)
        self.assertEqual(self.speakersCategoryHeaderSubHeadline, Utilities.SPEAKER_HEADER_SUB_HEADLINE_TEXT)
        self.assertEqual(self.speakersCategoryHeaderNote, Utilities.SPEAKER_HEADER_NOTE_TEXT)

    def test_successfully_loaded_all_speakers(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_speaker_category()

        self.speakersCategoryPage = CategoryResultsPage(self.driver)
        self.speakersNumber = self.speakersCategoryPage.get_number_of_elements_in_category()

        self.assertEqual(self.speakersNumber, 7)

    def tearDown(self):
        super().tearDown()


class Test_Laptops_Products_Category(Test_Products_Categories_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_loaded_laptop_header(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_laptop_category()

        self.laptopsCategoryPage = CategoryResultsPage(self.driver)
        self.laptopsCategoryHeaderHeadline = self.laptopsCategoryPage.get_text_of_header_headline()
        self.laptopsCategoryHeaderSubHeadline = self.laptopsCategoryPage.get_text_of_header_sub_headline()
        self.laptopsCategoryHeaderNote = self.laptopsCategoryPage.get_text_of_header_note()

        self.assertEqual(self.laptopsCategoryHeaderHeadline, Utilities.LAPTOP_HEADER_HEADLINE_TEXT)
        self.assertEqual(self.laptopsCategoryHeaderSubHeadline, Utilities.LAPTOP_HEADER_SUB_HEADLINE_TEXT)
        self.assertEqual(self.laptopsCategoryHeaderNote, Utilities.LAPTOP_HEADER_NOTE_TEXT)

    def test_successfully_loaded_all_laptops(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_laptop_category()

        self.laptopsCategoryPage = CategoryResultsPage(self.driver)
        self.laptopsNumber = self.laptopsCategoryPage.get_number_of_elements_in_category()

        self.assertEqual(self.laptopsNumber, 11)

    def tearDown(self):
        super().tearDown()


class Test_Tablets_Product_Category(Test_Products_Categories_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_loaded_tablet_header(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_tablet_category()

        self.tabletsCategoryPage = CategoryResultsPage(self.driver)
        self.tabletsCategoryHeaderHeadline = self.tabletsCategoryPage.get_text_of_header_headline()
        self.tabletsCategoryHeaderSubHeadline = self.tabletsCategoryPage.get_text_of_header_sub_headline()
        self.tabletsCategoryHeaderNote = self.tabletsCategoryPage.get_text_of_header_note()

        self.assertEqual(self.tabletsCategoryHeaderHeadline, Utilities.TABLET_HEADER_HEADLINE_TEXT)
        self.assertEqual(self.tabletsCategoryHeaderSubHeadline, Utilities.TABLET_HEADER_SUB_HEADLINE_TEXT)
        self.assertEqual(self.tabletsCategoryHeaderNote, Utilities.TABLET_HEADER_NOTE_TEXT)

    def test_successfully_loaded_all_tablets(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_tablet_category()

        self.tabletCategoryPage = CategoryResultsPage(self.driver)
        self.tabletsNumber = self.tabletCategoryPage.get_number_of_elements_in_category()

        self.assertEqual(self.tabletsNumber, 3)

    def tearDown(self):
        super().tearDown()


class Test_Mice_Product_Category(Test_Products_Categories_Base):

    def setUp(self):
        super().setUp()

    def test_successfully_loaded_mice_header(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_mice_category()

        self.miceCategoryPage = CategoryResultsPage(self.driver)
        self.miceCategoryHeaderHeadline = self.miceCategoryPage.get_text_of_header_headline()
        self.miceCategoryHeaderSubHeadline = self.miceCategoryPage.get_text_of_header_sub_headline()
        self.miceCategoryHeaderNote = self.miceCategoryPage.get_text_of_header_note()

        self.assertEqual(self.miceCategoryHeaderHeadline, Utilities.MICE_HEADER_HEADLINE_TEXT)
        self.assertEqual(self.miceCategoryHeaderSubHeadline, Utilities.MICE_HEADER_SUB_HEADLINE_TEXT)
        self.assertEqual(self.miceCategoryHeaderNote, Utilities.MICE_HEADER_NOTE_TEXT)

    def test_successfully_loaded_all_mice(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_mice_category()

        self.miceCategoryPage = CategoryResultsPage(self.driver)
        self.miceNumber = self.miceCategoryPage.get_number_of_elements_in_category()

        self.assertEqual(self.miceNumber, 9)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))
