import pytest


@pytest.mark.usefixtures("getDriver")
class BaseTest:

    def open(self, url):
        self.driver.get(url)
