from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_username_xpath = "//input[@id='Email']"
        self.textbox_password_xpath = "//input[@id='Password']"
        self.button_login_xpath = "//button[normalize-space()='Log in']"
        self.textmsg_invalid_xapth = "//li[normalize-space()='No customer account found']"
        self.textbox_usernameclear_xpath="//input[@id='Email']"
        self.textbox_passwordclear_xpath="//input[@id='Password']"

    def clear_usernametextbox(self):
        self.driver.find_element(By.XPATH,self.textbox_usernameclear_xpath).clear()

    def input_username(self,Username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(Username)

    def clear_passwordtextbox(self):
        self.driver.find_element(By.XPATH, self.textbox_passwordclear_xpath).clear()

    def input_password(self,Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def button_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def invalid_text(self):
        return self.driver.find_element(By.XPATH,self.textmsg_invalid_xapth).text
