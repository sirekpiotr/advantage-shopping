from Tests.unittest_products_categories import *

test_loader = unittest.TestLoader()
test_suit = unittest.TestSuite()

speakers_category = test_loader.loadTestsFromTestCase(Test_Speaker_Products_Category)
laptops_category = test_loader.loadTestsFromTestCase(Test_Laptops_Products_Category)
tablets_category = test_loader.loadTestsFromTestCase(Test_Tablets_Product_Category)
mice_category = test_loader.loadTestsFromTestCase(Test_Mice_Product_Category)
headphones_category = test_loader.loadTestsFromTestCase(Test_Headphone_Products_Category)

test_suit.addTests([
    speakers_category,
    laptops_category,
    tablets_category,
    mice_category,
    headphones_category
])

runner = HtmlTestRunner.HTMLTestRunner(output='../../Reports')
runner.run(test_suit)
