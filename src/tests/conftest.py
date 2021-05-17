import time

import pytest
from selenium import webdriver

from src import settings


# This will get the value from CLI /hooks
def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default=settings.BROWSER)
    parser.addoption("--env", action="store", default=settings.ENVIRONMENT)


# This will return the Browser value to setup method
@pytest.fixture()
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture()
def getDriver(request, getBrowser):
    _driver = None
    print("Browser Running : " + getBrowser)
    print("Running Environment : " + request.config.getoption("--env"))
    if getBrowser == "chrome":
        _driver = webdriver.Chrome(executable_path=settings.CHROME_EXECUTABLE_PATH)
    elif getBrowser == "Firefox":
        _driver = webdriver.Firefox(executable_path=settings.FIREFOX_EXECUTABLE_PATH)
    elif getBrowser == "Edge":
        _driver = webdriver.Edge(executable_path=settings.EDGE_EXECUTABLE_PATH)
    request.cls.driver = _driver

    yield request.cls.driver
    time.sleep(1)
    request.cls.driver.quit()


# PyTest HTML Report
# Hooks for adding environment information to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pranob Kalita'


# Hooks for delete/Modify environment information to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
