from selenium.webdriver.common.by import By


class GoogleHomePage:
    searchField = (By.XPATH, "//textarea[@title='Search']")
    searchButton = (By.XPATH, "//input[@aria-label='Google Search']")

    def __init__(self, driver):
        self.driver = driver

    def enter_search_query(self, query):
        self.driver.find_element(*GoogleHomePage.searchField).send_keys(query)

    def click_on_search_btn(self):
        self.driver.find_element(*GoogleHomePage.searchButton).click()
