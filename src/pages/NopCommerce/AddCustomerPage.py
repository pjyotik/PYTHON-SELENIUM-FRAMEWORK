import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    """ By Locators (Object Repository) """
    CUSTOMER_MENU_XPATH = "//a[@href='#']//p[contains(text(),'Customers')]"
    CUSTOMER_MENU_ITEM_XPATH = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    ADD_NEW_BTN_XPATH = "//a[normalize-space()='Add new']"
    EMAIL_XPATH = "//input[@id='Email']"
    PASSWORD_XPATH = "//input[@id='Password']"
    FIRST_NAME_XPATH = "//input[@id='FirstName']"
    LAST_NAME_XPATH = "//input[@id='LastName']"
    RADIO_BTN_GENDER_MALE_ID = "Gender_Male"
    RADIO_BTN_GENDER_FEMALE_ID = "Gender_Female"
    DOB_XPATH = "//input[@id='DateOfBirth']"
    COMPANY_NAME_XPATH = "//input[@id='Company']"
    CUSTOMER_ROLE_XPATH = "//div[@class='k-multiselect-wrap k-floatwrap']"
    LIST_ITEM_ADMINISTRATORS_XPATH = "//li[contains(text(),'Administrators')]"
    LIST_ITEM_REGISTERED_XPATH = "//li[contains(text(),'Registered')]"
    LIST_ITEM_GUESTS_XPATH = "//li[contains(text(),'Guests')]"
    LIST_ITEM_VENDORS_XPATH = "//li[contains(text(),'Vendors')]"
    DROPDOWN_MANAGER_OF_VENDOR = "//*[@id='VendorId']"
    ADMIN_CONTENT_XPATH = "//textarea[@id='AdminComment']"
    BTN_SAVE_XPATH = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.CUSTOMER_MENU_XPATH).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.CUSTOMER_MENU_ITEM_XPATH).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.ADD_NEW_BTN_XPATH).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.EMAIL_XPATH).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.PASSWORD_XPATH).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.CUSTOMER_ROLE_XPATH).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_REGISTERED_XPATH)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_ADMINISTRATORS_XPATH)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_GUESTS_XPATH)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_REGISTERED_XPATH)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_VENDORS_XPATH)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.LIST_ITEM_GUESTS_XPATH)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drop_down = Select(self.driver.find_element(By.XPATH, self.DROPDOWN_MANAGER_OF_VENDOR))
        drop_down.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.RADIO_BTN_GENDER_MALE_ID).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.RADIO_BTN_GENDER_FEMALE_ID).click()
        else:
            self.driver.find_element_by_id(self.RADIO_BTN_GENDER_MALE_ID).click()

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.FIRST_NAME_XPATH).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.LAST_NAME_XPATH).send_keys(lastName)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.DOB_XPATH).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.COMPANY_NAME_XPATH).send_keys(companyName)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.ADMIN_CONTENT_XPATH).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.BTN_SAVE_XPATH).click()
