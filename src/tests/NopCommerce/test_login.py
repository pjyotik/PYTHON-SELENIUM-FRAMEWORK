import pytest

from src.pages.NopCommerce.LoginPage import LoginPage
from src.tests.base_test import BaseTest
from src.util.Logger import LogGen

from src.util.PropertiesReader import ReadConfig


class Test_LoginPage(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_page_title(self):
        self.logger.info("***************** Verify Login Page Title *****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        actual_title = driver.title
        print("Page Title : ", actual_title)
        assert actual_title == ReadConfig.getLoginPageTitle()
        self.logger.info("***********************************************************")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self):
        self.logger.info("***************** Verify Successful Login to Application *****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        loginPage = LoginPage(driver)
        loginPage.set_username(ReadConfig.getUsername())
        loginPage.set_password(ReadConfig.getPassword())
        loginPage.click_login()
        actual_title = driver.title
        print("Page Title : ", actual_title)
        if actual_title == ReadConfig.getHomePageTitle():
            assert True
        else:
            driver.save_screenshot("./screenshots/" + "test_login.png")
            self.logger.info("***********************************************************")
            assert False
