from selenium.webdriver.common.by import By


class LoginPage:
    """ By Locators (Object Repository) """
    USERNAME_ID = "Email"
    PASSWORD_ID = "Password"
    LOGIN_BUTTON_XPATH = "//button[normalize-space()='Log in']"
    LOGOUT_LINK_TEXT = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.USERNAME_ID).clear()
        self.driver.find_element(By.ID, self.USERNAME_ID).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.PASSWORD_ID).clear()
        self.driver.find_element(By.ID, self.PASSWORD_ID).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.LOGOUT_LINK_TEXT).click()
