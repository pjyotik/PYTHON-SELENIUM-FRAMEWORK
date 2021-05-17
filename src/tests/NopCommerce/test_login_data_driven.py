import time

import pytest

from src.pages.NopCommerce.LoginPage import LoginPage
from src import settings
from src.tests.base_test import BaseTest
from src.util import ExcelUtils
from src.util.Logger import LogGen
from src.util.PropertiesReader import ReadConfig


class Test_LoginPage_DataDriven(BaseTest):
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_data_driven(self):
        self.logger.info("***************** Verify Successful Login to Application *****************")
        driver = self.driver
        driver.get(ReadConfig.getApplicationUrl())
        loginPage = LoginPage(driver)

        rows = ExcelUtils.getRowCount(settings.DATA_EXCEL, 'Sheet1')
        print("Number of Rows: ", rows)

        list_status = []  # Empty list variable

        for row in range(2, rows + 1):
            username = ExcelUtils.readData(settings.DATA_EXCEL, 'Sheet1', row, 1)
            password = ExcelUtils.readData(settings.DATA_EXCEL, 'Sheet1', row, 2)
            expected = ExcelUtils.readData(settings.DATA_EXCEL, 'Sheet1', row, 3)

            loginPage.set_username(username)
            loginPage.set_password(password)
            loginPage.click_login()
            time.sleep(5)

            actual_title = driver.title
            print("Actual Title : ", actual_title)
            expected_title = ReadConfig.getHomePageTitle()
            print("Expected Title : ", expected_title)

            if actual_title == expected_title:
                if expected == "Pass":
                    self.logger.info("*** Passed ***")
                    loginPage.click_logout()
                    list_status.append("Pass")
                elif expected == "Fail":
                    self.logger.info("*** Failed ***")
                    loginPage.click_logout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if expected == "Pass":
                    self.logger.info("*** Failed ***")
                    list_status.append("Fail")
                elif expected == "Fail":
                    self.logger.info("*** Passed ***")
                    list_status.append("Pass")
            print(list_status)
        if "Fail" not in list_status:
            self.logger.info("*** Login DataDriven Test is Passed ***")
            driver.close()
            assert True
        else:
            self.logger.info("*** Login DataDriven Test is Failed ***")
            driver.close()
            assert False

        self.logger.info("*******************************************************")
