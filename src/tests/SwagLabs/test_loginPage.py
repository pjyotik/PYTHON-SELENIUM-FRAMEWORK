import time
import os
from pathlib import Path

from src import settings
from src.pages.SwagLabs.HomePage import HomePage
from src.pages.SwagLabs.LoginPage import LoginPage
from src.tests.base_test import BaseTest
from src.util.Logger import LogGen

ROOT_DIR = os.path.dirname(Path(__file__).parent.parent.parent)
SCREENSHOTS_DIR = os.path.join(ROOT_DIR, "test-output", "screenshots")


class TestLogin(BaseTest):
    logger = LogGen.loggen()

    def test_valid_login(self):
        self.logger.info("***************** Verify Valid Login to Application *****************")
        driver = self.driver
        driver.get(settings.SAUCE_DEMO_APP_URL)
        loginPage = LoginPage(driver)
        loginPage.loginToApplication(settings.SAUCE_DEMO_APP_USERNAME, settings.SAUCE_DEMO_APP_PASSWORD)
        homePage = HomePage(driver)
        homePage.wait_for_product_text()

        actual_title = driver.title
        print("Page Title : ", actual_title)
        if actual_title == settings.SAUCE_DEMO_APP_TITLE:
            assert True
        else:
            driver.save_screenshot(SCREENSHOTS_DIR + "/SauceLabs_Valid_Login.png")
            self.logger.info("***********************************************************")
            assert False

    def test_invalid_login(self):
        self.logger.info("***************** Verify Invalid Login to Application *****************")
        driver = self.driver
        driver.get(settings.SAUCE_DEMO_APP_URL)
        loginPage = LoginPage(driver)
        loginPage.loginToApplication(settings.SAUCE_DEMO_APP_USERNAME_INVALID, settings.SAUCE_DEMO_APP_PASSWORD)
        time.sleep(1)
        error_text = loginPage.get_locked_error_text()
        print("Error Text : ", error_text)
        if error_text == settings.SAUCE_DEMO_APP_ERROR_MESSAGE:
            assert True
        else:
            driver.save_screenshot(SCREENSHOTS_DIR + "SauceLabs_Valid_Login.png")
            self.logger.info("***********************************************************")
            assert False
