import time

from selenium import webdriver
from testdata.data import *
from pages.loginpage import LoginPage
from pages.homepage import HomePage
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_un()
        lp.enter_pwd()
        lp.click_login()
        #lp.report_pass_fail

    def test_logout(self):
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(5)
        hp.logout_acti()
        #hp.report_pass_fail()
