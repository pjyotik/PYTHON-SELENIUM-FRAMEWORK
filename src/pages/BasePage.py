from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

""" This class is the parent of all pages """
""" It contains all the generic methods and utilities for all the pages """


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """  With this method we can avoid stale element exception """

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innerText")
        # element = self.wait.until(EC.presence_of_element_located(by_locator))
        # return element.text

    def is_visible(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

    def get_count(self, by_locator):
        return len(self.wait.until(EC.presence_of_all_elements_located(by_locator)))

    def get_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def select_by_text(self, by_locator, option):
        select = Select(self.get_element(by_locator))
        select.select_by_visible_text(option)
