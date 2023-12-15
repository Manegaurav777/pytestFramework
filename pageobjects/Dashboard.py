from selenium.webdriver.common.by import By


class Dashboard:

    def __init__(self,driver):
        self.driver=driver
        self.text_dashboard_xpath = "//h1[normalize-space()='Dashboard']"

    def welcome_msg(self):
        return self.driver.find_element(By.XPATH, self.text_dashboard_xpath).text
