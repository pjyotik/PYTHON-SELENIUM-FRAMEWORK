import time

import pytest

from src.pages.NopCommerce.AddCustomerPage import AddCustomerPage
from src.pages.NopCommerce.LoginPage import LoginPage
from src.pages.NopCommerce.SearchCustomer import SearchCustomer
from src.tests.base_test import BaseTest
from src.util.Logger import LogGen
from src.util.PropertiesReader import ReadConfig


class Test_SearchCustomer(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomer_byEmail(self):
        self.logger.info("***************** Search Customer[Email] Test Started *****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        driver.maximize_window()

        loginPage = LoginPage(driver)
        loginPage.set_username(ReadConfig.getUsername())
        loginPage.set_password(ReadConfig.getPassword())
        loginPage.click_login()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Search Customer By Email *****")

        addCustomer = AddCustomerPage(driver)
        addCustomer.clickOnCustomersMenu()
        addCustomer.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchCustomer = SearchCustomer(driver)
        searchCustomer.setEmail("victoria_victoria@nopCommerce.com")
        searchCustomer.clickSearch()
        time.sleep(5)
        status = searchCustomer.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert status  # status should be True
        self.logger.info("*************** Search Customer[Email] Test Finished *****************")
        driver.close()

    @pytest.mark.regression
    def test_searchCustomer_byName(self):
        self.logger.info("***************** Search Customer[Name] Test Started *****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        driver.maximize_window()

        loginPage = LoginPage(driver)
        loginPage.set_username(ReadConfig.getUsername())
        loginPage.set_password(ReadConfig.getPassword())
        loginPage.click_login()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Search Customer By Name *****")

        addCustomer = AddCustomerPage(driver)
        addCustomer.clickOnCustomersMenu()
        addCustomer.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by Name **********")
        searchCustomer = SearchCustomer(driver)
        searchCustomer.setFirstName("Victoria")
        searchCustomer.setLastName("Terces")
        searchCustomer.clickSearch()
        time.sleep(5)
        status = searchCustomer.searchCustomerByName("Victoria Terces")
        assert status
        self.logger.info("***************  Search Customer[Email] Test Finished *****************")
        driver.close()
