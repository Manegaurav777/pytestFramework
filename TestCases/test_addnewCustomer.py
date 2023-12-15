import time
from selenium.webdriver.common.by import By
import pytest
from pageobjects.Loginpage import Login

from pageobjects.newCustomer import NewCust
from utilities.Logger import LogGen

@pytest.mark.usefixtures("setup")
class TestNewCustomer(LogGen):
    def test_003(self):
        self.driver.maximize_window()
        lg = Login(self.driver)
        nc=NewCust(self.driver)
        log = self.loggen()
        lg.clear_usernametextbox()
        log.info("enter username")
        lg.input_username("admin@yourstore.com")

        lg.clear_passwordtextbox()
        log.info("enter password")
        lg.input_password("admin")
        lg.button_login()
        nc.click_custommerbutton()
        nc.click_innercustommerbutton()
        nc.addnew_customer()
        log.info("enter email")
        nc.enterEmail("ken21@gmail.com")
        log.info("enter password")
        nc.enterPassword("12345")
        log.info("enter Firstname")
        nc.enterFirstname("ken")
        log.info("enter lastname")
        nc.enterLastname("william")
        log.info("select gender")
        nc.select_Gender()
        log.info("select a date")
        nc.select_Calender()
        time.sleep(4)
        nc.select_date()
        log.info("date is selected")
        log.info("enter company name")
        nc.enterCompanyname("brisa")
        nc.select_tax()
        nc.Active_check()
        nc.Save_button()

        log.info("new customer is created")