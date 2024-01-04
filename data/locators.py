from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//*[@id='searchbox_input']")
    SEARCH_BUTTON = (By.XPATH, "//*[contains(@class,'searchbox_searchButton')]")
    RESULTS = (By.XPATH, "//article[@data-testid='result']")
