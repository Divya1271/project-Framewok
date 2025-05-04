import time

import pytest
from selenium import webdriver
from pageobjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    base_url=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("********    Test_001_Login *******")
        self.logger.info("******* Verifying login testcase *******")
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
            self.logger.info("******* Login testcase has passed *******")
        else:
            self.driver.save_screenshot(r"C:\Users\divya aghi\PycharmProjects\DesigningFramework\Screenshots"+ "test_login.png")
            self.driver.close()
            self.logger.error("******* Login testcase has failed*******")
            assert False
        print("Login Successful")





