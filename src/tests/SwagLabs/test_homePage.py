import os
import time
from pathlib import Path

from src import settings
from src.pages.SwagLabs.HomePage import HomePage
from src.pages.SwagLabs.LoginPage import LoginPage
from src.tests.base_test import BaseTest
from src.util import xlReader
from src.util.Logger import LogGen


class TestHome(BaseTest):
    logger = LogGen.loggen()

    def test_product_sorting(self):
        driver = self.driver
        driver.get(settings.SAUCE_DEMO_APP_URL)
        loginPage = LoginPage(driver)
        loginPage.loginToApplication(settings.SAUCE_DEMO_APP_USERNAME, settings.SAUCE_DEMO_APP_PASSWORD)
        homePage = HomePage(driver)
        homePage.wait_for_product_text()

        ROOT_DIR = os.path.dirname(Path(__file__).parent.parent.parent)
        TEST_DATA_DIR = os.path.join(ROOT_DIR, "test-data")
        print(TEST_DATA_DIR + settings.DATA_EXCEL)

        xlReader.load_excel(TEST_DATA_DIR + settings.DATA_EXCEL, "PRODUCT_SORT")
        data = xlReader.get_data_as_list_tuples()

        for item in data:
            homePage.select_item(item[0])
            time.sleep(1)
            assert homePage.get_first_item_name() == item[1]
            assert homePage.get_first_item_price() == ('$' + str(item[2]))
            time.sleep(1)

        time.sleep(2)

    def test_products_cart_count(self):
        driver = self.driver
        driver.get(settings.SAUCE_DEMO_APP_URL)
        loginPage = LoginPage(driver)
        loginPage.loginToApplication(settings.SAUCE_DEMO_APP_USERNAME, settings.SAUCE_DEMO_APP_PASSWORD)
        homePage = HomePage(driver)
        homePage.wait_for_product_text()

        # verify the product count
        print("Product count - " + str(homePage.get_items_count()))
        assert homePage.get_items_count() == 6

        # add couple of items and verify the cart count
        homePage.add_all_items_to_cart()
        print("cart count - " + homePage.get_cart_count())
        assert homePage.get_cart_count() == '6'
        time.sleep(3)

        # remove products from cart, verify the updated count
        homePage.remove_first_item_from_cart()
        homePage.remove_second_item_from_cart()
        assert homePage.get_cart_count() == '4'

        time.sleep(3)
