import random
import string
import pytest

from src.pages.NopCommerce.AddCustomerPage import AddCustomerPage
from src.pages.NopCommerce.LoginPage import LoginPage
from src.tests.base_test import BaseTest
from src.util.Logger import LogGen
from src.util.PropertiesReader import ReadConfig


class Test_AddCustomer(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self):
        self.logger.info("***************** Add New Customer Test Started*****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        driver.maximize_window()

        loginPage = LoginPage(driver)
        loginPage.set_username(ReadConfig.getUsername())
        loginPage.set_password(ReadConfig.getPassword())
        loginPage.click_login()
        self.logger.info("***** Login Successful *****")
        actual_title = driver.title
        print("Page Title : ", actual_title)

        addCustomer = AddCustomerPage(driver)
        addCustomer.clickOnCustomersMenu()
        addCustomer.clickOnCustomersMenuItem()
        addCustomer.clickOnAddNew()

        self.logger.info("***** Providing Customer Information *****")

        self.email = self.get_random_string(10) + "@gmail.com"
        print("Email ID entered is : ", self.email)
        addCustomer.setEmail(self.email)
        addCustomer.setPassword("test123")
        addCustomer.setCustomerRoles("Guests")
        addCustomer.setManagerOfVendor("Vendor 2")
        addCustomer.setGender("Male")
        addCustomer.setFirstName("ABC")
        addCustomer.setLastName("LIMITED")
        addCustomer.setDob("7/05/1985")
        addCustomer.setCompanyName("ABC Limited")
        addCustomer.setAdminContent("Automation Testing Using Python")
        addCustomer.clickOnSave()
        self.logger.info("***** Saving Customer Information *****")

        self.logger.info("********* Add Customer Validation Started *****************")

        self.msg = driver.find_element_by_tag_name("body").text
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add Customer Test Passed *********")
        else:
            driver.save_screenshot("./screenshots/" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add Customer Test Failed ************")
            assert False

        driver.close()
        self.logger.info("******* Ending Add Customer Test **********")

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result = ''.join(random.choice(letters) for i in range(length))
        return result
