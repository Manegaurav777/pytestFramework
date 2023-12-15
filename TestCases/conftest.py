from selenium import webdriver
import pytest


@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    yield
    request.cls.driver.quit()
