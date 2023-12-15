from selenium.webdriver.common.by import By


class NewCust:
    def __init__(self, driver):
        self.driver=driver
        self.Customer_button_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
        self.Customers_button_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
        self.add_new_button_xpath="//a[normalize-space()='Add new']"
        self.input_email_xpath="//input[@id='Email']"
        self.input_password_xpath="//input[@id='Password']"
        self.firstname_xpath="//input[@id='FirstName']"
        self.lastname_xapth="//input[@id='LastName']"
        self.gender_xpath="//input[@id='Gender_Male']"
        self.calender_icon="//span[@class='k-icon k-i-calendar']"
        self.date_xpath="/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[4]/a[1]"
        self.companyname_xpath="//input[@id='Company']"
        self.taxbutton_xpath="//input[@id='IsTaxExempt']"
        self.activecheck_xpath="//input[@id='Active']"
        self.save_button_xpath="//button[@name='save']"


    def click_custommerbutton(self):
        self.driver.find_element(By.XPATH,self.Customer_button_xpath).click()

    def click_innercustommerbutton(self):
        self.driver.find_element(By.XPATH, self.Customers_button_xpath).click()

    def addnew_customer(self):
        self.driver.find_element(By.XPATH, self.add_new_button_xpath).click()

    def enterEmail(self,email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def enterFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(firstname)

    def enterLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_xapth).send_keys(lastname)

    def select_Gender(self):
        self.driver.find_element(By.XPATH, self.gender_xpath).click()

    def select_Calender(self):
        self.driver.find_element(By.XPATH, self.calender_icon).click()

    def select_date(self):
        self.driver.find_element(By.XPATH,self.date_xpath).click()

    def enterCompanyname(self, companyname):
        self.driver.find_element(By.XPATH, self.companyname_xpath).send_keys(companyname)

    def select_tax(self):
        self.driver.find_element(By.XPATH, self.taxbutton_xpath).click()

    def Active_check(self):
        self.driver.find_element(By.XPATH, self.activecheck_xpath).click()

    def Save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()








