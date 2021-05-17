import configparser
import os
from pathlib import Path

""" This class is to read the config details from config.ini file """

ROOT_DIR = os.path.dirname(Path(__file__).parent)
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
print("CONFIG FILE PATH : " + CONFIG_DIR + "/config.ini")

config = configparser.RawConfigParser()
config.read(CONFIG_DIR + "/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('NOP_Commerce_Application', 'BASE_URL')
        return url

    @staticmethod
    def getLoginPageTitle():
        login_page_title = config.get('NOP_Commerce_Application', 'LOGIN_PAGE_TITLE')
        return login_page_title

    @staticmethod
    def getUsername():
        username = config.get('NOP_Commerce_Application', 'USERNAME')
        return username

    @staticmethod
    def getPassword():
        password = config.get('NOP_Commerce_Application', 'PASSWORD')
        return password

    @staticmethod
    def getHomePageTitle():
        home_page_title = config.get('NOP_Commerce_Application', 'HOME_PAGE_TITLE')
        return home_page_title

    @staticmethod
    def getEnvironment():
        env = config.get('Environment_Variables', 'ENVIRONMENT')
        return env

    @staticmethod
    def getBrowser():
        browser = config.get('Environment_Variables', 'BROWSER')
        return browser

    @staticmethod
    def getChromeExecutablePath():
        executable_path = config.get('Environment_Variables', 'CHROME_EXECUTABLE_PATH')
        return executable_path

    @staticmethod
    def getFirefoxExecutablePath():
        executable_path = config.get('Environment_Variables', 'FIREFOX_EXECUTABLE_PATH')
        return executable_path

    @staticmethod
    def getEdgeExecutablePath():
        executable_path = config.get('Environment_Variables', 'EDGE_EXECUTABLE_PATH')
        return executable_path

    @staticmethod
    def getTestDataExcelPath():
        execl_path = config.get('Environment_Variables', 'DATA_EXCEL')
        return execl_path
