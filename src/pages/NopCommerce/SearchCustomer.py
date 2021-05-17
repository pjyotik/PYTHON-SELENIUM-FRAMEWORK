from selenium.webdriver.common.by import By


class SearchCustomer:
    """ By Locators (Object Repository) """
    EMAIL_ID = "SearchEmail"
    FIRSTNAME_ID = "SearchFirstName"
    LASTNAME_ID = "SearchLastName"
    CUSTOMER_SEARCH_BTN_ID = "search-customers"
    TABLE_SEARCH_RESULT_XPATH = "//table[@role='grid']"
    TABLE_XPATH = "//table[@id='customers-grid']"
    TABLE_ROWS_XPATH = "//table[@id='customers-grid']//tbody/tr"
    TABLE_COLUMNS_XPATH = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.EMAIL_ID).clear()
        self.driver.find_element(By.ID, self.EMAIL_ID).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.FIRSTNAME_ID).clear()
        self.driver.find_element(By.ID, self.FIRSTNAME_ID).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.LASTNAME_ID).clear()
        self.driver.find_element(By.ID, self.LASTNAME_ID).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.CUSTOMER_SEARCH_BTN_ID).click()

    def getNoOfRows(self):
        element = self.driver.find_elements(By.XPATH, self.TABLE_ROWS_XPATH)
        return len(element)

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.TABLE_COLUMNS_XPATH))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.TABLE_XPATH)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.TABLE_XPATH)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
