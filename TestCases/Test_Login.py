import time
from selenium.webdriver.common.by import By
import pytest
from pageobjects.Loginpage import Login
from pageobjects.Dashboard import Dashboard
from utilities.Logger import LogGen


@pytest.mark.usefixtures("setup")
class TestLogin(LogGen):
    def test_001(self):
        self.driver.maximize_window()
        lg=Login(self.driver)
        db=Dashboard(self.driver)
        log = self.loggen()
        log.info("testcase_001 starting")
        lg.clear_usernametextbox()
        lg.input_username("admin@yourstore.com")
        log.info("entering username")
        lg.clear_passwordtextbox()
        lg.input_password("admin")
        log.info("entering password")
        lg.button_login()

        time.sleep(4)
        if "Dashboard" in db.welcome_msg():
            assert True
            log.info("found keyword, test case is passeed")
        else:
            assert False
        print("passed")


    def test_002(self,):

        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.co")



        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        time.sleep(4)
        if "No customer account found" in self.driver.find_element(By.XPATH,"//li[normalize-space()='No customer account found']").text:

            assert True



        else:
            assert False
        print("passed")

