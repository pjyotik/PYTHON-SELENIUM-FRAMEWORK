from selenium.webdriver.common.by import By

from src.pages.BasePage import BasePage


class LoginPage(BasePage):

    """ Constructor of the page class """
    def __init__(self, driver):
        super().__init__(driver)

    username_ID = (By.ID, "user-name")
    password_ID = (By.ID, "password")
    loginButton_ID = (By.ID, "login-button")
    locked_error_text = (By.CSS_SELECTOR, "h3[data-test='error']")

    """ Page Actions """
    def loginToApplication(self, username, password):
        self.send_keys(self.username_ID, username)
        self.send_keys(self.password_ID, password)
        self.click(self.loginButton_ID)

    def get_locked_error_text(self):
        return self.get_text(self.locked_error_text)
