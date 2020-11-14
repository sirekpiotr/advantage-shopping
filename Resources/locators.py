from selenium.webdriver.common.by import By


class Locators:

    # ---- HOME SITE ----

    HOME_PAGE_OUR_PRODUCTS_CONTAINER = (By.ID, "container")
    HOME_SEARCH_BUTTON = (By.ID, "search")
    HOME_SEARCH_FIELD = (By.ID, "autoComplete")
    HOME_SEARCH_FIELD_CLOSE_BUTTON = (By.XPATH, "//*[@id='search']/div/div/img")
    HOME_HEADPHONE_CATEGORY_BUTTON = (By.ID, 'headphonesTxt')
    HOME_SPEAKER_CATEGORY_BUTTON = (By.ID, 'speakersTxt')
    HOME_TABLETS_CATEGORY_BUTTON = (By.ID, 'tabletsTxt')
    HOME_LAPTOPS_CATEGORY_BUTTON = (By.ID, 'laptopsTxt')
    HOME_MICE_CATEGORY_BUTTON = (By.ID, 'miceTxt')
    HOME_USER_LOGIN_BUTTON = (By.ID, 'hrefUserIcon')
    HOME_POPUP = (By.CLASS_NAME, 'PopUp')
    HOME_POPUP_USERNAME_FIELD = (By.NAME, 'username')
    HOME_POPUP_PASSWORD_FIELD = (By.NAME, 'password')
    HOME_POPUP_SUBMIT_BUTTON = (By.ID, 'sign_in_btnundefined')

    # ---- SEARCH RESULTS -----

    SEARCH_RESULTS_HEADLINE = (By.ID, 'searchResultLabel')
    SEARCH_FAILED_HEADLINE = (By.CLASS_NAME, 'noProducts')

    # ---- CATEGORIES ----

    CATEGORY_HEADER = (By.CLASS_NAME, 'categoryData')
    CATEGORY_HEADER_HEADLINE = (By.XPATH, "//div[contains(@class, 'categoryData')]/h1")
    CATEGORY_HEADER_SUB_HEADLINE = (By.XPATH, "//div[contains(@class, 'categoryData')]/h2")
    CATEGORY_HEADER_NOTE = (By.XPATH, "//div[contains(@class, 'categoryData')]/h3")

    # ---- PRODUCTS ----

    PRODUCT_IMAGE = (By.CLASS_NAME, 'imgProduct')
    PRODUCT_NAME_HEADLINE = (By.CLASS_NAME, 'productName')






