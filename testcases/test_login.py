import time

import pytest
from selenium import webdriver
from pageobjects.LoginPage import Login
from utilities.readProperties import ReadConfig

class Test_001_Login:
    base_url=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    def test_homepagetitle(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        time.sleep(2)
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
        else:
            assert False
        print("We are on login page")

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False
        print("Login Successful")





